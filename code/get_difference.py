def get_difference(bi_, lo_):

    return lo_[bi_ == 1].sum() - lo_[bi_ == 0].sum()
