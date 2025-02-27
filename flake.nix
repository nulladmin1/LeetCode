{
  description = "LeetCode Solutions";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    poetry2nix.url = "github:nix-community/poetry2nix";
  };

  outputs = {
    self,
    nixpkgs,
    poetry2nix,
  }: let
    systems = ["x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin"];
    forEachSystem = nixpkgs.lib.genAttrs systems;
    pkgs = forEachSystem (system: import nixpkgs {inherit system;});
  in {
    formatter = forEachSystem (system: nixpkgs.legacyPackages.${system}.alejandra);

    devShells = forEachSystem (system: {
      default = pkgs.${system}.mkShell {
        packages = with pkgs.${system}; [
          python3
          poetry
        ];
      };
    });

    apps = forEachSystem (system: let
      inherit (poetry2nix.lib.mkPoetry2Nix {pkgs = pkgs.${system};}) mkPoetryApplication;
      leetcode = mkPoetryApplication {projectDir = ./.;};
    in {
      default = {
        type = "app";
        program = "${leetcode}/bin/two_sum";
      };
      two_sum = {
        type = "app";
        program = "${leetcode}/bin/two_sum";
      };
      merge_strings_alternatively = {
        type = "app";
        program = "${leetcode}/bin/merge_strings_alternatively";
      };
      range_sum_query_immutable = {
        type = "app";
        program = "${leetcode}/bin/range_sum_query_immutable";
      };
    });
  };
}
