_base_ = [
    '../_base_/models/denseclip_r50.py', '../_base_/datasets/pascal_voc12_aug_20.py', 
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_20k.py'
]
model = dict(
    decode_head=dict(
        text_categories=20, 
        text_channels=1024, 
        text_embeddings_path='pretrain/voc_RN50_clip_text.pth',
        visual_projs_path='pretrain/RN50_clip_weights.pth',
    ),
)