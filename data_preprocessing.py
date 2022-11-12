# %%
from pytorch_lightning import seed_everything
import wandb
import torch
from app.lightning_data_module.aoi import AOI as AOI_LDM
from shutil import copy2


seed = 0
seed_everything(seed, workers=True)
wandb.init(mode="disabled")

ldm = AOI_LDM(
    work_dir="/dataB1/tommie_kerssies/",
    seed=seed,
    batch_size=1,
    val_batch_size=1,
    num_workers=2,
    crop_size=None,
    augment=False,
    pin_memory=False,
    scale_factor=1.0,
).setup()

# %%
# num_non_ignore = 0
# num_ignore = 0
# for batch in ldm.train_dataloader():
#     img_path, mask_path, ignore_mask = (
#         batch["img_path"][0],
#         batch["mask_path"][0],
#         batch["ignore_mask"][0],
#     )
#     if torch.count_nonzero(ignore_mask) > 0:
#         num_ignore += 1
#     else:
#         num_non_ignore += 1
#         copy2(img_path, "/dataB1/tommie_kerssies/multilabel_v6/train_non_ignore/img/")
#         copy2(mask_path, "/dataB1/tommie_kerssies/multilabel_v6/train_non_ignore/lbl/")
#     print(
#         f"num_non_ignore: {num_non_ignore}, num_ignore: {num_ignore}",
#         end="\r",
#     )
# print()

# %%
# num_buffer0 = 0
# num_buffer1 = 0
# for batch in ldm.train_dataloader():
#     img_path, mask_path = (
#         batch["img_path"][0],
#         batch["mask_path"][0],
#     )
#     if "buffer00" in img_path:
#         num_buffer0 += 1
#         copy2(
#             img_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/train_buffer00/img/",
#         )
#         copy2(
#             mask_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/train_buffer00/lbl/",
#         )
#     else:
#         num_buffer1 += 1
#     print(
#         f"num_buffer0: {num_buffer0}, num_buffer1: {num_buffer1}",
#         end="\r",
#     )
# print()

# %%
# num_no_wire = 0
# num_wire = 0
# for batch in ldm.train_dataloader():
#     img_path, mask_path, wire_mask = (
#         batch["img_path"][0],
#         batch["mask_path"][0],
#         batch["masks"][0][0],
#     )
#     if torch.count_nonzero(wire_mask) > 0:
#         num_wire += 1
#         copy2(
#             img_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/train_buffer00_only_wire/img/",
#         )
#         copy2(
#             mask_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/train_buffer00_only_wire/lbl/",
#         )
#     else:
#         num_no_wire += 1
#     print(
#         f"num_wire: {num_wire}, num_no_wire: {num_no_wire}",
#         end="\r",
#     )
# print()

#%% ---------------------------------------------------------------------------------------------------------------------------------------------
# num_cropped = 0
# num_not_cropped = 0
# for batch in ldm.val_dataloader():
#     img_tensor, img_path, mask_path = (
#         batch["image"][0],
#         batch["img_path"][0],
#         batch["mask_path"][0],
#     )
#     if img_tensor.shape[-1] == 4096:
#         num_cropped += 1
#         import cv2
#         from pathlib import Path

#         img = cv2.imread(img_path)
#         mask = cv2.imread(mask_path)
#         for r in range(0, img.shape[0], 2048):
#             for c in range(0, img.shape[1], 2048):
#                 cv2.imwrite(
#                     img_path.replace(".bmp", f"_{r}_{c}.bmp").replace(
#                         "/val/", "/val_cropped/"
#                     ),
#                     img[r : r + 2048, c : c + 2048, :],
#                 )
#                 cv2.imwrite(
#                     mask_path.replace(".png", f"_{r}_{c}.png").replace(
#                         "/val/", "/val_cropped/"
#                     ),
#                     mask[r : r + 2048, c : c + 2048, :],
#                 )
#     else:
#         copy2(img_path, "/dataB1/tommie_kerssies/multilabel_v6/val_cropped/img/")
#         copy2(mask_path, "/dataB1/tommie_kerssies/multilabel_v6/val_cropped/lbl/")
#         num_not_cropped += 1
#     print(
#         f"num_not_cropped: {num_not_cropped}, num_cropped: {num_cropped}",
#         end="\r",
#     )
# print()

# %%
# num_non_ignore = 0
# num_ignore = 0
# for batch in ldm.val_dataloader():
#     img_path, mask_path, ignore_mask = (
#         batch["img_path"][0],
#         batch["mask_path"][0],
#         batch["ignore_mask"][0],
#     )
#     if torch.count_nonzero(ignore_mask) > 0:
#         num_ignore += 1
#     else:
#         num_non_ignore += 1
#         copy2(
#             img_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/val_cropped_non_ignore/img/",
#         )
#         copy2(
#             mask_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/val_cropped_non_ignore/lbl/",
#         )
#     print(
#         f"num_non_ignore: {num_non_ignore}, num_ignore: {num_ignore}",
#         end="\r",
#     )
# print()

# %%
# num_buffer0 = 0
# num_buffer1 = 0
# for batch in ldm.val_dataloader():
#     img_path, mask_path = (
#         batch["img_path"][0],
#         batch["mask_path"][0],
#     )
#     if "buffer00" in img_path:
#         num_buffer0 += 1
#         copy2(
#             img_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/val_cropped_buffer00/img/",
#         )
#         copy2(
#             mask_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/val_cropped_buffer00/lbl/",
#         )
#     else:
#         num_buffer1 += 1
#     print(
#         f"num_buffer0: {num_buffer0}, num_buffer1: {num_buffer1}",
#         end="\r",
#     )
# print()

#%%
# num_no_wire = 0
# num_wire = 0
# for batch in ldm.val_dataloader():
#     img_path, mask_path, wire_mask = (
#         batch["img_path"][0],
#         batch["mask_path"][0],
#         batch["masks"][0][0],
#     )
#     if torch.count_nonzero(wire_mask) > 0:
#         num_wire += 1
#         copy2(
#             img_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/val_cropped_buffer00_only_wire/img/",
#         )
#         copy2(
#             mask_path,
#             "/dataB1/tommie_kerssies/multilabel_v6/val_cropped_buffer00_only_wire/lbl/",
#         )
#     else:
#         num_no_wire += 1
#     print(
#         f"num_wire: {num_wire}, num_no_wire: {num_no_wire}",
#         end="\r",
#     )
# print()

# %%
# num_cropped = 0
# num_not_cropped = 0
# size_before = 2048
# size_after = 256
# old_dir = "val_cropped_buffer00_only_wire"
# new_dir = "val_cropped_buffer00_only_wire_256"
# for batch in ldm.val_dataloader():
#     img_tensor, img_path, mask_path = (
#         batch["image"][0],
#         batch["img_path"][0],
#         batch["mask_path"][0],
#     )
#     if img_tensor.shape[-1] == size_before:
#         num_cropped += 1
#         import cv2
#         from pathlib import Path

#         img = cv2.imread(img_path)
#         mask = cv2.imread(mask_path)
#         for r in range(0, img.shape[0], size_after):
#             for c in range(0, img.shape[1], size_after):
#                 cv2.imwrite(
#                     img_path.replace(".bmp", f"_{r}_{c}.bmp").replace(old_dir, new_dir),
#                     img[r : r + size_after, c : c + size_after, :],
#                 )
#                 cv2.imwrite(
#                     mask_path.replace(".png", f"_{r}_{c}.png").replace(
#                         old_dir, new_dir
#                     ),
#                     mask[r : r + size_after, c : c + size_after, :],
#                 )
#     else:
#         copy2(
#             img_path,
#             f"/dataB1/tommie_kerssies/multilabel_v6/{new_dir}/img/",
#         )
#         copy2(
#             mask_path,
#             f"/dataB1/tommie_kerssies/multilabel_v6/{new_dir}/lbl/",
#         )
#         num_not_cropped += 1
#     print(
#         f"num_not_cropped: {num_not_cropped}, num_cropped: {num_cropped}",
#         end="\r",
#     )
# print()