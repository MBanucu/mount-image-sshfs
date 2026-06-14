# mount-image-sshfs — AGENTS.md

## Project

Disk image mounting via SSHFS (cross-platform FUSE).

- **Package**: `mount-image-sshfs` (PyPI), `mount_image_sshfs` (import)
- **Repo**: `https://github.com/MBanucu/mount-image-sshfs`
- **Python**: `>=3.10`
- **License**: GPL-3.0-only

## Commands

```bash
pip install -e .
python -m unittest discover -s tests -v
pip install coverage
python -m coverage run -m unittest discover -s tests -v
python -m coverage report --fail-under=70 --skip-covered
```

## Module structure

```
mount_image_sshfs/
  __init__.py    — public API
tests/
  test_mount_image_sshfs.py
```
