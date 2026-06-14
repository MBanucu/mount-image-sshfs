"""Disk image mounting via SSHFS (cross-platform FUSE)."""

import os
import shutil
import subprocess
import tempfile


def mount_image(source: str, fstype: str | None = None,
                options: list[str] | None = None) -> tuple[str, str]:
    """Mount *source* via SSHFS.

    *source* is a remote path like ``user@host:/remote/path``.
    Returns ``(mount_point, mount_point)`` — both values are the same
    since SSHFS uses FUSE without a separate block device.
    Raises ``RuntimeError`` on failure.
    """
    mount_point = tempfile.mkdtemp(prefix='mount_image_')
    cmd = ['sshfs', source, mount_point]
    if options:
        for opt in options:
            cmd.extend(['-o', opt])

    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        shutil.rmtree(mount_point, ignore_errors=True)
        raise RuntimeError(f"sshfs mount failed: {r.stderr}")

    return mount_point, mount_point


def umount_image(device: str, mount_point: str | None = None):
    """Unmount a FUSE filesystem."""
    mp = mount_point or device
    for cmd in (['fusermount', '-u', mp], ['umount', mp]):
        r = subprocess.run(cmd, capture_output=True)
        if r.returncode == 0:
            break
    try:
        shutil.rmtree(mp, ignore_errors=True)
    except Exception:
        pass


def attach_image(image_path: str) -> str:
    """Not supported — SSHFS does not create block devices."""
    raise NotImplementedError("SSHFS does not create block devices")


def detach_image(device: str):
    """Not supported — SSHFS does not create block devices."""
    raise NotImplementedError("SSHFS does not create block devices")


def umount_inner(mount_point: str):
    """Unmount FUSE without cleanup. Used by the orchestrator."""
    for cmd in (['fusermount', '-u', mount_point], ['umount', mount_point]):
        r = subprocess.run(cmd, capture_output=True)
        if r.returncode == 0:
            break


def detach_inner(device: str):
    """No-op. SSHFS uses FUSE, no loop device to detach."""
    pass
