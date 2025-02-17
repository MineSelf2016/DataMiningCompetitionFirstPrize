from commons import variables


def validate(prediction_y_list, actual_y_list):

    right_num_dict = {}
    prediction_num_dict = {}
    actual_num_dict = {}

    for (p_y, a_y) in zip(prediction_y_list, actual_y_list):
        if not p_y in prediction_num_dict.keys():
            prediction_num_dict[p_y] = 0
        prediction_num_dict[p_y] += 1

        if not a_y in actual_num_dict.keys():
            actual_num_dict[a_y] = 0
        actual_num_dict[a_y] += 1

        if p_y == a_y:
            if not p_y in right_num_dict.keys():
                right_num_dict[p_y] = 0
            right_num_dict[p_y] += 1

    return right_num_dict,prediction_num_dict,actual_num_dict
