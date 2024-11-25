{
  description = ''
    Development environment for fast api speed test project, providing essential tools like Bash and Python.
  '';

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
    in {
      devShells."${system}".default = let
        pkgs = import nixpkgs {
          inherit system;
        };
      in pkgs.mkShell {
        packages = with pkgs; [
          bashInteractiveFHS
          pkg-config

          # Tests
          python3
          python312Packages.httpx
  
          # fastAPI
          python312Packages.fastapi
          python312Packages.uvicorn

          # flask
          python312Packages.flask

          # expressJs
          nodejs_22

        ];

        shellHook = ''
          # Set up Wayland library path and notify user
          export LD_LIBRARY_PATH=${pkgs.wayland}/lib:$LD_LIBRARY_PATH
          echo "Welcome to the fast-api-speed-test development shell!"
          echo "Included tools:"
          echo "- Bash and Python"
        '';
      };
    };
}
