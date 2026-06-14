{ lib, buildPythonPackage, setuptools, src }:
buildPythonPackage rec {
  pname = "mount-image-sshfs";
  version = "0.1.0";
  pyproject = true;
  inherit src;
  nativeBuildInputs = [ setuptools ];
  propagatedBuildInputs = [ ];
  doCheck = false;
  pythonImportsCheck = [ "mount_image_sshfs" ];
  meta = with lib; {
    description = "Disk image mounting via SSHFS (cross-platform FUSE)";
    homepage = "https://github.com/MBanucu/mount-image-sshfs";
    license = licenses.gpl3Only;
    maintainers = with maintainers; [ ];
  };
}
