"""Unit tests for mount_image_sshfs — mocked subprocess calls."""

import unittest
from unittest.mock import patch, MagicMock


class TestSshfsMount(unittest.TestCase):
    @patch('mount_image_sshfs.subprocess.run')
    @patch('mount_image_sshfs.tempfile.mkdtemp')
    def test_mount_image_success(self, mock_mkdtemp, mock_run):
        mock_mkdtemp.return_value = '/tmp/mp'
        mock_run.return_value = MagicMock(returncode=0, stderr='')
        from mount_image_sshfs import mount_image
        dev, mp = mount_image('user@host:/path', None, None)
        self.assertEqual(dev, '/tmp/mp')
        self.assertEqual(mp, '/tmp/mp')

    @patch('mount_image_sshfs.subprocess.run')
    @patch('mount_image_sshfs.tempfile.mkdtemp')
    def test_mount_image_fails(self, mock_mkdtemp, mock_run):
        mock_mkdtemp.return_value = '/tmp/mp'
        mock_run.return_value = MagicMock(returncode=1, stderr='failed')
        from mount_image_sshfs import mount_image
        with self.assertRaises(RuntimeError) as ctx:
            mount_image('user@host:/path', None, None)
        self.assertIn('sshfs mount failed', str(ctx.exception))

    @patch('mount_image_sshfs.subprocess.run')
    @patch('mount_image_sshfs.tempfile.mkdtemp')
    def test_mount_image_with_options(self, mock_mkdtemp, mock_run):
        mock_mkdtemp.return_value = '/tmp/mp'
        mock_run.return_value = MagicMock(returncode=0)
        from mount_image_sshfs import mount_image
        mount_image('user@host:/path', None, ['ro', 'noatime'])
        args = mock_run.call_args[0][0]
        self.assertIn('-o', args)
        self.assertIn('ro', args)

    @patch('mount_image_sshfs.subprocess.run')
    def test_umount_image(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)
        from mount_image_sshfs import umount_image
        umount_image('/tmp/mp')

    def test_attach_image_raises(self):
        from mount_image_sshfs import attach_image
        with self.assertRaises(NotImplementedError):
            attach_image('/tmp/test.img')

    def test_detach_image_raises(self):
        from mount_image_sshfs import detach_image
        with self.assertRaises(NotImplementedError):
            detach_image('/dev/loop0')

    @patch('mount_image_sshfs.subprocess.run')
    def test_umount_inner(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)
        from mount_image_sshfs import umount_inner
        umount_inner('/tmp/mp')

    def test_detach_inner_noop(self):
        from mount_image_sshfs import detach_inner
        detach_inner('/tmp/mp')
