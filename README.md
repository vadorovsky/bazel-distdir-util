# bazel-distdir-util

Utility for pre-fetching dependencies for Bazel

## How to use

Go to the directory with project which uses Bazel, in example:

```
cd envoy
```

Then use the tool:

```
$ bazel-distdir-util
https://github.com/bazelbuild/bazel-gazelle/archive/0.14.0.tar.gz
https://github.com/google/boringssl/archive/060e9a583976e73d1ea8b2bfe8b9cab33c62fa17.tar.gz
https://github.com/abseil/abseil-cpp/archive/92e07e5590752d6b8e67f7f2f86c6286561e8cea.tar.gz
https://files.pythonhosted.org/packages/c6/b4/510617906f8e0c5660e7d96fbc5585113f83ad547a3989b80297ac72a74c/thrift-0.11.0.tar.gz
https://github.com/bombela/backward-cpp/archive/v1.4.tar.gz
https://github.com/circonus-labs/libcircllhist/archive/fd8a14463739d247b414825cc56ca3946792a3b9.tar.gz
https://github.com/Cyan4973/xxHash/archive/v0.6.5.tar.gz
https://github.com/eile/tclap/archive/tclap-1-2-1-release-final.tar.gz
https://github.com/fmtlib/fmt/archive/5.2.1.tar.gz
https://github.com/gabime/spdlog/archive/v1.2.1.tar.gz
https://github.com/gcovr/gcovr/archive/3.3.tar.gz
https://github.com/google/libprotobuf-mutator/archive/c3d2faf04a1070b0b852b0efdef81e1a81ba925e.tar.gz
https://github.com/grpc/grpc/archive/v1.15.0.tar.gz
https://github.com/nanopb/nanopb/archive/f8ac463766281625ad710900479130c7fcb4d63b.tar.gz
https://github.com/opentracing/opentracing-cpp/archive/v1.5.0.tar.gz
https://github.com/lightstep/lightstep-tracer-cpp/archive/v0.8.0.tar.gz
https://github.com/googleapis/googleapis/archive/d6f78d948c53f3b400bb46996eb3084359914f9b.tar.gz
https://github.com/google/jwt_verify_lib/archive/66792a057ec54e4b75c6a2eeda4e98220bd12a9a.tar.gz
https://github.com/nodejs/http-parser/archive/77310eeb839c4251c07184a5db8885a572a08352.tar.gz
https://github.com/pallets/jinja/archive/2.10.tar.gz
https://github.com/pallets/markupsafe/archive/1.0.tar.gz
https://github.com/Tencent/rapidjson/archive/v1.1.0.tar.gz
https://files.pythonhosted.org/packages/08/bc/d6409a813a9dccd4920a6262eb6e5889e90381453a5f58938ba4cf1d9420/twitter.common.lang-0.3.9.tar.gz
https://files.pythonhosted.org/packages/be/97/f5f701b703d0f25fbf148992cd58d55b4d08d3db785aad209255ee67e2d0/twitter.common.rpc-0.3.9.tar.gz
https://files.pythonhosted.org/packages/f9/e7/4f80d582578f8489226370762d2cf6bc9381175d1929eba1754e03f70708/twitter.common.finagle-thrift-0.3.9.tar.gz
https://github.com/google/googletest/archive/release-1.8.1.tar.gz
https://github.com/protocolbuffers/protobuf/archive/fa252ec2a54acb24ddc87d48fed1ecfd458445fd.tar.gz
https://github.com/grpc-ecosystem/grpc-httpjson-transcoding/archive/05a15e4ecd0244a981fdf0348a76658def62fa9c.tar.gz
https://github.com/golang/protobuf/archive/31e0d063dd98c052257e5b69eeb006818133f45c.tar.gz
https://github.com/bazelbuild/rules_go/archive/3d966375ff7971d43b863f785f495c7dcd6923da.tar.gz
https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz#md5=34eed507548117b2ab523ab14b2f8b55
https://github.com/google/subpar/archive/1.3.0.tar.gz
https://github.com/bazelbuild/bazel-skylib/archive/0.5.0.tar.gz
https://github.com/lyft/protoc-gen-validate/archive/30da78c4bcdd477b3c24d13e43cf39361ae3859f.tar.gz
https://github.com/googleapis/googleapis/archive/d642131a6e6582fc226caf9893cb7fe7885b3411.tar.gz
https://github.com/gogo/protobuf/archive/v1.1.1.tar.gz
https://github.com/prometheus/client_model/archive/99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c.tar.gz
https://github.com/census-instrumentation/opencensus-proto/archive/ab82e5fdec8267dc2a726544b10af97675970847.tar.gz
```

You can use `--rpmspec-format` to generate `SourceX` lines which you can paste
into your RPM spec:

```
$ bazel-distdir-util --rpmspec-format
Source0: https://github.com/bazelbuild/bazel-gazelle/archive/0.14.0.tar.gz
Source1: https://github.com/google/boringssl/archive/060e9a583976e73d1ea8b2bfe8b9cab33c62fa17.tar.gz
Source2: https://github.com/abseil/abseil-cpp/archive/92e07e5590752d6b8e67f7f2f86c6286561e8cea.tar.gz
Source3: https://files.pythonhosted.org/packages/c6/b4/510617906f8e0c5660e7d96fbc5585113f83ad547a3989b80297ac72a74c/thrift-0.11.0.tar.gz
Source4: https://github.com/bombela/backward-cpp/archive/v1.4.tar.gz
Source5: https://github.com/circonus-labs/libcircllhist/archive/fd8a14463739d247b414825cc56ca3946792a3b9.tar.gz
Source6: https://github.com/Cyan4973/xxHash/archive/v0.6.5.tar.gz
Source7: https://github.com/eile/tclap/archive/tclap-1-2-1-release-final.tar.gz
Source8: https://github.com/fmtlib/fmt/archive/5.2.1.tar.gz
Source9: https://github.com/gabime/spdlog/archive/v1.2.1.tar.gz
Source10: https://github.com/gcovr/gcovr/archive/3.3.tar.gz
Source11: https://github.com/google/libprotobuf-mutator/archive/c3d2faf04a1070b0b852b0efdef81e1a81ba925e.tar.gz
Source12: https://github.com/grpc/grpc/archive/v1.15.0.tar.gz
Source13: https://github.com/nanopb/nanopb/archive/f8ac463766281625ad710900479130c7fcb4d63b.tar.gz
Source14: https://github.com/opentracing/opentracing-cpp/archive/v1.5.0.tar.gz
Source15: https://github.com/lightstep/lightstep-tracer-cpp/archive/v0.8.0.tar.gz
Source16: https://github.com/googleapis/googleapis/archive/d6f78d948c53f3b400bb46996eb3084359914f9b.tar.gz
Source17: https://github.com/google/jwt_verify_lib/archive/66792a057ec54e4b75c6a2eeda4e98220bd12a9a.tar.gz
Source18: https://github.com/nodejs/http-parser/archive/77310eeb839c4251c07184a5db8885a572a08352.tar.gz
Source19: https://github.com/pallets/jinja/archive/2.10.tar.gz
Source20: https://github.com/pallets/markupsafe/archive/1.0.tar.gz
Source21: https://github.com/Tencent/rapidjson/archive/v1.1.0.tar.gz
Source22: https://files.pythonhosted.org/packages/08/bc/d6409a813a9dccd4920a6262eb6e5889e90381453a5f58938ba4cf1d9420/twitter.common.lang-0.3.9.tar.gz
Source23: https://files.pythonhosted.org/packages/be/97/f5f701b703d0f25fbf148992cd58d55b4d08d3db785aad209255ee67e2d0/twitter.common.rpc-0.3.9.tar.gz
Source24: https://files.pythonhosted.org/packages/f9/e7/4f80d582578f8489226370762d2cf6bc9381175d1929eba1754e03f70708/twitter.common.finagle-thrift-0.3.9.tar.gz
Source25: https://github.com/google/googletest/archive/release-1.8.1.tar.gz
Source26: https://github.com/protocolbuffers/protobuf/archive/fa252ec2a54acb24ddc87d48fed1ecfd458445fd.tar.gz
Source27: https://github.com/grpc-ecosystem/grpc-httpjson-transcoding/archive/05a15e4ecd0244a981fdf0348a76658def62fa9c.tar.gz
Source28: https://github.com/golang/protobuf/archive/31e0d063dd98c052257e5b69eeb006818133f45c.tar.gz
Source29: https://github.com/bazelbuild/rules_go/archive/3d966375ff7971d43b863f785f495c7dcd6923da.tar.gz
Source30: https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz#md5=34eed507548117b2ab523ab14b2f8b55
Source31: https://github.com/google/subpar/archive/1.3.0.tar.gz
Source32: https://github.com/bazelbuild/bazel-skylib/archive/0.5.0.tar.gz
Source33: https://github.com/lyft/protoc-gen-validate/archive/30da78c4bcdd477b3c24d13e43cf39361ae3859f.tar.gz
Source34: https://github.com/googleapis/googleapis/archive/d642131a6e6582fc226caf9893cb7fe7885b3411.tar.gz
Source35: https://github.com/gogo/protobuf/archive/v1.1.1.tar.gz
Source36: https://github.com/prometheus/client_model/archive/99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c.tar.gz
Source37: https://github.com/census-instrumentation/opencensus-proto/archive/ab82e5fdec8267dc2a726544b10af97675970847.tar.gz
```

## TODO

Features which will be implemented soon:

- downloading archives
- genraring the whole RPM spec
