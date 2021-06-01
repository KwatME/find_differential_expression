def get_log_ratio(bi_, lo_):

    return lo_[bi_ == 1].mean() - lo_[bi_ == 0].mean()
