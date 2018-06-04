
from DetectContour.diagram.parse_image_segments_neha import parse_image_segments
from DetectContour.utils.prep import open_image



def test_parse_image_segments():

    image_segment_parse = parse_image_segments(open_image('t1.png'))
    image_segment_parse.diagram_image_segment.display_binarized_segmented_image()
    for idx, label_image_segment in image_segment_parse.label_image_segments.iteritems():
        label_image_segment.display_segmented_image()


if __name__ == "__main__":
     test_parse_image_segments()

