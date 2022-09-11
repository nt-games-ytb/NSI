# Filius - Simple Network Simulation
Filius is a network simulator for educational purpose

## Licencse
Filius is provided under the terms of GPLv2 or GPLv3.

## Requirements
Filius is a Java application. It is required that there is a Java Runtime Environment 8 or higher. Support of Java 8 is deprecated and will end soon.

For most features, JRE will do. The feature to implement and run your own applications (by means of the Software Wizard) requires Java Development Kit.

## OS Support
Windows, Linux

## Available Languages
German, French, English

## Configuration
The personal configuration, i.e. selected language as well as the ui state when leaving the program, is stored within the personal home directory within a folder named ".filius".

Global configurations can be modified in the install directory within "filius.ini". For more details see the documented parameter in this file.

## Installation
The Windows installer is based on nsis. It supports the standard parameter:
* /S - for silent install/uninstall
* /D - to set the install directory (e.g. /D=Z:\Filius)

## Website
https://www.lernsoftware-filius.de/

# Bundled JRE
Some Filius distributions are shipped with JRE to remove the external dependency on a pre-installed Java Runtime Environment. But since Filius is not built as a Java module, the JRE cannot be built as part of the build process with Maven.

The Runtime is created in two steps:
0. Define required Java modules
0. Create the runtime

## Define Required Modules
Use the jdeps tool that is shipped with OpenJDK:

```
jdeps -recursive --ignore-missing-deps --multi-release base --print-module-deps filius.jar lib\*
```

The output contains some warnings and the following required modules:

```
java.base,java.compiler,java.desktop,java.instrument,java.management,java.naming,java.sql,java.xml.crypto,jdk.unsupported
```

Additionally, the following runtime dependencies are required in order to use the Software Assistant for application compilation at runtime in Filius:
- jdk.compiler - This module contains the compiler toolset.
- jdk.zipfs - This module is required to read dependencies on built-in Filius classes from filius.jar.

## Build Runtime
The bundled JRE (if available) is built with the following command:

```
jlink --no-header-files --no-man-pages --compress=2 --strip-debug --add-modules java.base,java.desktop,java.instrument,java.management,java.naming,java.sql,java.xml.crypto,jdk.unsupported,java.compiler,jdk.compiler,jdk.zipfs --output java-runtime
```
