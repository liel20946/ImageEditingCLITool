import filters
BOX_BLUR_TYPE = "box_blur"
EDGE_DETECTION_TYPE = "edge_detection"
SHARPEN_TYPE = "sharpen"
GREY_SCALE_TYPE = "grey_scale"


def create_filter(filter_name, *args):
    if filter_name == BOX_BLUR_TYPE:
        return filters.BoxBlur(*args)
    elif filter_name == EDGE_DETECTION_TYPE:
        return filters.EdgeDetection()
    elif filter_name == SHARPEN_TYPE:
        return filters.Sharpen(*args)
    elif filter_name == GREY_SCALE_TYPE:
        return filters.GreyScale()
    else:
        raise ValueError("Invalid filter type")