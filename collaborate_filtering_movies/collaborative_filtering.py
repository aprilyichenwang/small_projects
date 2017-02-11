import argparse
import pandas as pd
import numpy as np
import time


def parse_argument():
    """
    Code for parsing arguments
    """
    parser = argparse.ArgumentParser(description='Parsing a file.')
    parser.add_argument('--train', nargs=1, required=True)
    parser.add_argument('--test', nargs=1, required=True)
    args = vars(parser.parse_args())
    return args


def parse_file(filename):
    """
    Given a filename outputs user_ratings and movie_ratings dictionaries

    Input: filename

    Output: user_ratings, movie_ratings
        where:
            user_ratings[user_id] = {movie_id: rating}
            movie_ratings[movie_id] = {user_id: rating}

    """
    # user_ratings={139540:{8:2.0},1205593:{8:4.0}}
    # movie_ratings={8:{139540:2.0, 1205593:2.0},17742:{139540:4.0,1205593:3.0}}

    user_ratings = {}
    movie_ratings = {}

    train_df = pd.read_csv(filename,
                           header=None,
                           names=['MovieId', 'CustomerId', 'Rating'])
    Movies = train_df['MovieId'].unique()  # an array
    for m in Movies:
        per_movie_ratings_dic = train_df[train_df['MovieId'] == m].set_index('CustomerId').to_dict()
        movie_ratings[m] = per_movie_ratings_dic['Rating']
   

    Users = train_df['CustomerId'].unique()
    for u in Users:
        per_user_raings_dic = train_df[train_df['CustomerId'] == u].set_index('MovieId').to_dict()
        user_ratings[u] = per_user_raings_dic['Rating']

    return user_ratings, movie_ratings


def compute_average_user_ratings(user_ratings):
    """ Given a the user_rating dict compute average user ratings

    Input: user_ratings (dictionary of user, movies, ratings)
    Output: ave_ratings (dictionary of user and ave_ratings)
    """
    ave_ratings = {}
    # Your code here
    for u in user_ratings:
        ave_ratings[u] = float(sum(user_ratings[u].values())) / len(user_ratings[u].values())
    return ave_ratings


def compute_user_similarity(d1, d2, ave_rat1, ave_rat2):
    """ Computes similarity between two users

        Input: d1, d2, (dictionary of user ratings per user) 
            ave_rat1, ave_rat2 average rating per user (float)
        Ouput: user similarity (float)
    """
    # Your code here

    if len(set(d1.keys()) & set(d2.keys())) < 1:
        print "no common movies between two users"
        return 0.0
    else:
        movies = set(d1.keys()) & set(d2.keys())

    numerator = 0
    denominator1, denominator2 = 0, 0
    for m in movies:
        numerator += (d1[m] - ave_rat1) * (d2[m] - ave_rat2)
        denominator1 += (d1[m] - ave_rat1) ** 2
        denominator2 += (d2[m] - ave_rat2) ** 2

    # catch the zero denominator situation
    if denominator1 == 0 or denominator2 == 0:
        w = 0
    else:
        w = float(numerator) / ((denominator1 * denominator2) ** 0.5)
    return w


def predict_movie_ratings_given_user_movie(movie_to_predict, user_to_predict,
                                           movie_ratings, user_ratings, ave_ratings):
    # given movie k, find all users that have watched that movie
    # iterate all these users,
    # sum up all results- (User j's rating for that movie k - ave rating for that user j) *similarity between J & I,
    # sum of wij,take the division, add the average rating of Ri
    # output the predicted ratings

    # user_ratings={139540:{8:2.0},1205593:{8:4.0}}
    # movie_ratings={8:{139540:2.0, 1205593:2.0},17742:{139540:4.0,1205593:3.0}}

    wij_dic = {}
    numerator = 0
    denominator = 0
    all_js = movie_ratings[movie_to_predict]
    R_ave_user_to_predict = ave_ratings[user_to_predict]

    for j in all_js:
        j_rating = user_ratings[j][movie_to_predict]
        ave_j = ave_ratings[j]

        if (user_to_predict,j) not in wij_dic:
            w = compute_user_similarity(user_ratings[j], user_ratings[user_to_predict],
                                        ave_ratings[j],ave_ratings[user_to_predict])
            wij_dic[(user_to_predict,j)] = w
        else:
            w=wij_dic[(user_to_predict,j)]

        numerator += (j_rating - ave_j) * w
        denominator += abs(w)

    try:
        R_user_to_predict = R_ave_user_to_predict + float(numerator) / denominator
    except:
        R_user_to_predict = R_ave_user_to_predict

    return R_user_to_predict


def calculate_RMSE(m1, m2):
    RMSE = round((float(sum((m1 - m2) * (m1 - m2))) / len(m1)) ** 0.5, 4)
    return RMSE


def calculate_MAE(m1, m2):
    MAE = round(float(sum(abs(m1 - m2))) / len(m1), 4)
    return MAE


def main():
    """
    This function is called from the command line via
    
    python cf.py --train [path to filename] --test [path to filename]
    """
    args = parse_argument()
    train_file = args['train'][0]
    test_file = args['test'][0]

    user_ratings, movie_ratings = parse_file(train_file)
    ave_ratings = compute_average_user_ratings(user_ratings)

    test_df = pd.read_csv(test_file, header=None, names=['MovieId', 'CustomerId', 'Rating'])

    for row in range(len(test_df)):
        if row % 100 == 0:
            print "the %sth row" % row
        movie = int(test_df.ix[row, 0])
        user_to_predict = int(test_df.ix[row, 1])
        R_ik = predict_movie_ratings_given_user_movie(movie, user_to_predict, movie_ratings, user_ratings, ave_ratings)
        test_df.ix[row, 'Prediction'] = R_ik

    test_df.to_csv('predictions.txt')
    true_ratings = test_df.ix[:, 'Rating'].as_matrix()
    prediction = test_df.ix[:, 'Prediction'].as_matrix()
    print "RMSE", calculate_RMSE(true_ratings, prediction)
    print "MAE", calculate_MAE(true_ratings, prediction)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print "time elapsed :%s mins" % ((time.time() - start_time) / 60)
