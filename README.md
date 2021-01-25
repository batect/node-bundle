# node-bundle

[![Build Status](https://img.shields.io/github/workflow/status/batect/node-bundle/Pipeline/main)](https://github.com/batect/node-bundle/actions?query=workflow%3APipeline+branch%3Amain)
[![License](https://img.shields.io/github/license/batect/node-bundle.svg)](https://opensource.org/licenses/Apache-2.0)

A bundle for [Batect](https://batect.dev) that provides a development container for Node.js, with sensible default configuration.

## Usage

### Setup

Add the following to your `batect.yml`:

```yaml
include:
  - type: git
    repo: https://github.com/batect/node-bundle.git
    ref: XXX # Replace with latest version from https://github.com/batect/node-bundle/releases
```

### Containers

#### `node-build-env`

A container (based on the official [Node.js images](https://hub.docker.com/_/node)) with sensible defaults for use with Node.js.

It mounts the project directory into the container, enables run as current user mode and configures a cache for dependencies downloaded by NPM or Yarn.

### Example

```
tasks:
  build:
    description: Start the application
    group: Test tasks
    run:
      container: node-build-env
      command: yarn start

include:
  - type: git
    repo: https://github.com/batect/node-bundle.git
    ref: XXX # Replace with latest version from https://github.com/batect/node-bundle/releases
```

The [TypeScript sample project](https://github.com/batect/batect-sample-typescript) also demonstrates how to use this bundle.

## Development

Run `./batect --list-tasks` to see a list of available tasks for this project.
