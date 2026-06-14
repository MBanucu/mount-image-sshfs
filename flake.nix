{
  description = "mount-image-sshfs: Disk image mounting via SSHFS (cross-platform FUSE)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { self
    , nixpkgs
    , flake-utils
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [ self.overlays.default ];
        };
      in
      {
        packages.default = pkgs.python3.pkgs.mount-image-sshfs;
        devShells.default = pkgs.mkShell {
          inputsFrom = [ pkgs.python3.pkgs.mount-image-sshfs ];
          packages = [ pkgs.python3 ];
          shellHook = ''
            echo "mount-image-sshfs dev shell. Run tests:"
            echo "  python -m unittest discover -s tests -v"
          '';
        };
      }
    )
    // {
      overlays.default = final: prev: {
        mount-image-sshfs = final.python3.pkgs.callPackage ./default.nix {
          src = final.lib.cleanSource ./.;
        };
        python3 = prev.python3.override {
          packageOverrides = _: _: { inherit (final) mount-image-sshfs; };
        };
      };
    };
}
