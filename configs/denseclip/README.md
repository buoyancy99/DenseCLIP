# DenseCLIP: Extract Free Dense Labels from CLIP

## Abstract
<!-- [ABSTRACT] -->
Contrastive Language-Image Pre-training (CLIP) has made a remarkable breakthrough in open-vocabulary zero-shot image recognition. Many recent studies leverage the pre-trained CLIP models for image-level classification and manipulation. In this paper, we further explore the potentials of CLIP for pixel-level dense prediction, specifically in semantic segmentation. Our method, DenseCLIP, in the absence of annotations and fine-tuning, yields reasonable segmentation results on open concepts across various datasets. By adding pseudo labeling and self-training, DenseCLIP+ surpasses SOTA transductive zero-shot semantic segmentation methods by large margins, e.g., mIoUs of unseen classes on PASCAL VOC/PASCAL Context/COCO Stuff are improved from 35.6/20.7/30.3 to 86.1/66.7/54.7. We also test the robustness of DenseCLIP under input corruption and evaluate its capability in discriminating fine-grained objects and novel concepts. Our finding suggests that DenseCLIP can serve as a new reliable source of supervision for dense prediction tasks to achieve annotation-free segmentation.

## Results and models of annotation-free segmentation

### Pascal VOC 2012 + Aug (w/o Background)

| Method    | CLIP Model | Crop Size | mIoU | config                                           |
| --------- | ---------- | --------- |----: | -------------------------------------------------|
| DenseCLIP | R-50       | 512x512   | 41.5 | [config](denseclip_r50_512x512_voc12aug_20.py)   |
| DenseCLIP | R-50x16    | 512x512   | 50.9 | [config](denseclip_r50x16_512x512_voc12aug_20.py)|


### Pascal Context (w/o Background)

| Method    | CLIP Model | Crop Size | mIoU | config                                                 |
| --------- | ---------- | --------- |----: | -------------------------------------------------------|
| DenseCLIP | R-50       | 480x480   | 18.5 | [config](denseclip_r50_480x480_pascal_context_59.py)   |
| DenseCLIP | R-50x16    | 480x480   | 20.3 | [config](denseclip_r50x16_480x480_pascal_context_59.py)|


### COCO-Stuff 164k

| Method    | CLIP Model | Crop Size | mIoU | config                                              |
| --------- | ---------- | --------- |----: | ----------------------------------------------------|
| DenseCLIP | R-50       | 512x512   | 10.5 | [config](denseclip_r50_512x512_coco-stuff164k.py)   |
| DenseCLIP | R-50x16    | 512x512   | 13.6 | [config](denseclip_r50x16_512x512_coco-stuff164k.py)|


### ADE20K

| Method    | CLIP Model | Crop Size | mIoU | config                                      |
| --------- | ---------- | --------- |----: | --------------------------------------------|
| DenseCLIP | R-50       | 512x512   |  8.3 | [config](denseclip_r50_512x512_ade20k.py)   |
| DenseCLIP | R-50x16    | 512x512   | 10.5 | [config](denseclip_r50x16_512x512_ade20k.py)|


### Pascal VOC 2012 + Aug (Under Corruption)

| Method    | CLIP Model | Crop Size | Corrupt Type | Corrupt Level | mIoU | config                                                   |
| --------- | ---------- | --------- | ------------ | ------------- |----: | ---------------------------------------------------------|
| DenseCLIP | R-50       | 512x512   | Speckle Noise| 1             | 30.9 | [config](denseclip_r50_512x512_voc12aug_20_corrupt.py)   |
