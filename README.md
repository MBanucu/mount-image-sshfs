# mount-image-sshfs

Disk image mounting via SSHFS (cross-platform FUSE).

[![PyPI version](https://img.shields.io/pypi/v/mount-image-sshfs)](https://pypi.org/project/mount-image-sshfs/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/MBanucu/mount-image-sshfs)](LICENSE)
[![OS](https://img.shields.io/badge/OS-Linux%20%7C%20macOS-blue)](https://github.com/MBanucu/mount-image-sshfs)

[![CI](https://img.shields.io/github/actions/workflow/status/MBanucu/mount-image-sshfs/test.yml?branch=main)](https://github.com/MBanucu/mount-image-sshfs/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/MBanucu/mount-image-sshfs/branch/main/graph/badge.svg)](https://codecov.io/gh/MBanucu/mount-image-sshfs)

## Quick start

```python
from mount_image_sshfs import mount_image, umount_image

mount_point, _ = mount_image('user@host:/remote/path')
print(f'Mounted at {mount_point}')
umount_image(mount_point, mount_point)
```

## API

- `mount_image(source, fstype=None, options=None)` → `(mount_point, mount_point)`
- `umount_image(mount_point, mount_point=None)`
- `attach_image(path)` — raises `NotImplementedError`
- `detach_image(device)` — raises `NotImplementedError`

Requires `sshfs` installed on the host.

## License

GPL-3.0-only
