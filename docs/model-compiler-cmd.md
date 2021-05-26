OVERVIEW:  The Glow compiler

Glow is a compiler for neural network accelerators.

USAGE: model-compiler [options]

OPTIONS:

Bundle Options:

  -bundle-api                                                                     - Specify which bundle API to use.
    =dynamic                                                                      -   Dynamic API
    =static                                                                       -   Static API
  -bundle-api-verbose                                                             - Print more details in the bundle API header file

Color Options:

  -color                                                                          - Use colors in output (default=autodetect)

General options:

  -aarch64-neon-syntax                                                            - Choose style of NEON code to emit from AArch64 backend:
    =generic                                                                      -   Emit generic NEON assembly
    =apple                                                                        -   Emit Apple-style NEON assembly
  -amdgpu-dpp-combine                                                             - Enable DPP combiner
  -amdgpu-dump-hsa-metadata                                                       - Dump AMDGPU HSA Metadata
  -amdgpu-enable-global-sgpr-addr                                                 - Enable use of SGPR regs for GLOBAL LOAD/STORE instructions
  -amdgpu-enable-merge-m0                                                         - Merge and hoist M0 initializations
  -amdgpu-sdwa-peephole                                                           - Enable SDWA peepholer
  -amdgpu-spill-sgpr-to-smem                                                      - Use scalar stores to spill SGPRs if supported by subtarget
  -amdgpu-verify-hsa-metadata                                                     - Verify AMDGPU HSA Metadata
  -amdgpu-vgpr-index-mode                                                         - Use GPR indexing mode instead of movrel for vector indexing
  -arm-add-build-attributes                                                       - 
  -arm-implicit-it                                                                - Allow conditional instructions outdside of an IT block
    =always                                                                       -   Accept in both ISAs, emit implicit ITs in Thumb
    =never                                                                        -   Warn in ARM, reject in Thumb
    =arm                                                                          -   Accept in ARM, reject in Thumb
    =thumb                                                                        -   Warn in ARM, emit implicit ITs in Thumb
  -atomic-counter-update-promoted                                                 - Do counter update using atomic fetch add  for promoted counters only
  -bundle-objects=<string>                                                        - Comma separated list of names of other object files which should be archived into the bundle. The object files are pre registered during Glow build. 
  -compilation-log                                                                - Dump Compilation Log
  -cpu-memory=<uint>                                                              - CPU DeviceManager maximum memory in kilobytes.
  -cvp-dont-process-adds                                                          - 
  -disable-promote-alloca-to-lds                                                  - Disable promote alloca to LDS
  -disable-promote-alloca-to-vector                                               - Disable promote alloca to vector
  -do-counter-promotion                                                           - Do counter register promotion
  -emscripten-cxx-exceptions-whitelist=<string>                                   - The list of function names in which Emscripten-style exception handling is enabled (see emscripten EMSCRIPTEN_CATCHING_WHITELIST options)
  -enable-cse-in-irtranslator                                                     - Should enable CSE in irtranslator
  -enable-cse-in-legalizer                                                        - Should enable CSE in Legalizer
  -enable-emscripten-cxx-exceptions                                               - WebAssembly Emscripten-style exception handling
  -enable-emscripten-sjlj                                                         - WebAssembly Emscripten-style setjmp/longjmp handling
  -enable-gvn-memdep                                                              - 
  -enable-load-pre                                                                - 
  -enable-loop-simplifycfg-term-folding                                           - 
  -enable-name-compression                                                        - Enable name string compression
  -expensive-combines                                                             - Enable expensive instruction combines
  -float-abi                                                                      - Option to set float ABI type
    =default                                                                      -   Default float ABI type
    =soft                                                                         -   Soft float ABI (softfp)
    =hard                                                                         -   Hard float ABI (hardfp)
  -gpsize=<uint>                                                                  - Global Pointer Addressing Size.  The default size is 8.
  -hash-based-counter-split                                                       - Rename counter variable of a comdat function based on cfg hash
  -instcombine-code-sinking                                                       - Enable code sinking
  -instcombine-guard-widening-window=<uint>                                       - How wide an instruction window to bypass looking for another guard
  -instcombine-max-num-phis=<uint>                                                - Maximum number phis to handle in intptr/ptrint folding
  -instcombine-maxarray-size=<uint>                                               - Maximum array size considered when doing a combine
  -instrprof-atomic-counter-update-all                                            - Make all profile counter updates atomic (for testing only)
  -internalize-public-api-file=<filename>                                         - A file containing list of symbol names to preserve
  -internalize-public-api-list=<list>                                             - A list of symbol names to preserve
  -iterative-counter-promotion                                                    - Allow counter promotion across the whole loop nest.
  -llvm-compiler=<string>                                                         - External LLVM compiler (e.g. llc) to use for compiling LLVM bitcode into machine code
  -llvm-compiler-opt=<string>                                                     - Options to pass to the external LLVM compiler
  -llvm-opt=<string>                                                              - External LLVM-Opt compiler (opt) to use for optimizing LLVM bitcode.
  -mabi=<string>                                                                  - Machine ABI to be used
  -march=<string>                                                                 - LLVM architecture to be used
  -max-counter-promotions=<int>                                                   - Max number of allowed counter promotions
  -max-counter-promotions-per-loop=<uint>                                         - Max number counter promotions per loop to avoid increasing register pressure too much
  -mcpu=<string>                                                                  - LLVM CPU to be used
  -memop-size-large=<uint>                                                        - Set large value thresthold in memory intrinsic size profiling. Value of 0 disables the large value profiling.
  -memop-size-range=<string>                                                      - Set the range of size in memory intrinsic calls to be profiled precisely, in a format of <start_val>:<end_val>
  -merror-missing-parenthesis                                                     - Error for missing parenthesis around predicate registers
  -merror-noncontigious-register                                                  - Error for register names that aren't contigious
  -mhvx                                                                           - Enable Hexagon Vector eXtensions
    =v60                                                                          -   Build for HVX v60
    =v62                                                                          -   Build for HVX v62
    =v65                                                                          -   Build for HVX v65
    =v66                                                                          -   Build for HVX v66
    =                                                                             -   
  -mips-compact-branches                                                          - MIPS Specific: Compact branch policy.
    =never                                                                        -   Do not use compact branches if possible.
    =optimal                                                                      -   Use compact branches where appropiate (default).
    =always                                                                       -   Always use compact branches if possible.
  -mips16-constant-islands                                                        - Enable mips16 constant islands.
  -mips16-hard-float                                                              - Enable mips16 hard float.
  -mno-compound                                                                   - Disable looking for compound instructions for Hexagon
  -mno-fixup                                                                      - Disable fixing up resolved relocations for Hexagon
  -mno-ldc1-sdc1                                                                  - Expand double precision loads and stores to their single precision counterparts
  -mno-pairing                                                                    - Disable looking for duplex instructions for Hexagon
  -mwarn-missing-parenthesis                                                      - Warn for missing parenthesis around predicate registers
  -mwarn-noncontigious-register                                                   - Warn for register names that arent contigious
  -mwarn-sign-mismatch                                                            - Warn for mismatching a signed and unsigned value
  -nvptx-sched4reg                                                                - NVPTX Specific: schedule for register pressue
  -partitioner_enable_load_balance                                                - Enable a partitioner pass to optimize for load balance in addition to memory capacity constraints
  -pseudo-random-seed                                                             - Seed for pseudo-random numbers
  -r600-ir-structurize                                                            - Use StructurizeCFG IR pass
  -rdf-dump                                                                       - 
  -rdf-limit=<uint>                                                               - 
  -sample-profile-check-record-coverage=<N>                                       - Emit a warning if less than N% of records in the input profile are matched to the IR.
  -sample-profile-check-sample-coverage=<N>                                       - Emit a warning if less than N% of samples in the input profile are matched to the IR.
  -sample-profile-max-propagate-iterations=<uint>                                 - Maximum number of iterations to go through when propagating sample block/edge weights through the CFG.
  -speculative-counter-promotion-max-exiting=<uint>                               - The max number of exiting blocks of a loop to allow  speculative counter promotion
  -speculative-counter-promotion-to-loop                                          - When the option is false, if the target block is in a loop, the promotion will be disallowed unless the promoted counter  update can be further/iteratively promoted into an acyclic  region.
  -target=<string>                                                                - LLVM target triple to be used
  -target-feature=<string>                                                        - LLVM target/CPU features to be used
  -verbose-compilation                                                            - Log empty passes to Compilation Log
  -verify-region-info                                                             - Verify region info (time consuming)
  -vp-counters-per-site=<number>                                                  - The average number of profile counters allocated per value profiling site.
  -vp-static-alloc                                                                - Do static counter allocation for value profiler

Generic Options:

  -help                                                                           - Display available options (-help-hidden for more)
  -help-list                                                                      - Display list of available options (-help-list-hidden for more)
  -version                                                                        - Display the version of this program

Glow Backend Utils Options:

  -reuse-activation-memory-allocations                                            - Should activation memory allocations be reused

Glow CPU Backend Options:

  -bundle-code-model                                                              - Specify which code model to use for a bundle
    =small                                                                        -   Small code model
    =medium                                                                       -   Medium code model
    =large                                                                        -   Large code model
  -code-model                                                                     - Specify which code model to use on the target machine
    =small                                                                        -   Small code model
    =medium                                                                       -   Medium code model
    =large                                                                        -   Large code model
  -dump-jit-symbol-info                                                           - Dump the load addresses and sizes of JITted symbols
  -dump-llvm-asm                                                                  - Dump the textual assembly of the jitted code
  -dump-llvm-ir                                                                   - Dump the LLVM-IR of the jitted code
  -g                                                                              - Emit debug information for debuggers
  -jit-specialize                                                                 - Create specialized functions for operations with constant dimensions
  -relocation-model                                                               - Specify which relocation model to use on the target machine
    =static                                                                       -   Non-relocatable code
    =pic                                                                          -   Position independent code

Glow Flags Lib CmdLine Options:

  -enable-DRT                                                                     - Deprecated. Enabled DRT support. Alias to glow_enable_drt.
  -enable-P2P                                                                     - Deprecated. Enabled P2P support. Alias to glow_enable_drt.

Glow Interpreter Backend Options:

  -interpreter-memory=<uint>                                                      - Interpreter DeviceManager maximum memory in kilobytes

Glow Partitioner Options:

  -dump-partition                                                                 - Enable dumping the graph of each partitions
  -log-partition                                                                  - Enable logging partition info

Graph Optimizations Options:

  -const-dedup-size=<uint>                                                        - Max number of elements allowed for deduplicating Constants. A value equal to 0 means no limit. Default is 0.

Graph Scheduler Options:

  Scheduler to use:
    -child-mem-size-based                                                         - Use ChildMemSizeBased
    -topological-sort-based                                                       - Use TopologicalSortBased

HostManager Options:

  -device_init_timeout_ms=<uint>                                                  - Set device init timout in milliseconds
  -load-backend-specific-opts=<options.yaml>                                      - Load backend-specific options for compilation.
  -load-device-configs=<configs.yaml>                                             - Load device configs used in Runtime

How to export the Glow Intermediate Representation/Graphs:
These options are for debugging the graphs by writing the IR/Graphs to given files/stdout

  -dump-graph                                                                     - Prints Graph to stdout
  -dump-graph-DAG=<file.dot>                                                      - Specify the file to export the Graph in DOT format
  -dump-graph-DAG-before-compile=<file.dot>                                       - Specify the file to export the Graph in DOT format

IR Optimizer Options:

  -dump-ir                                                                        - Prints IR to stdout
  -instrument-debug                                                               - Instrument the IR for debugging
  -instrument-debug-dir=<string>                                                  - The directory where the file dumps will be written!
  -instrument-debug-format=<string>                                               - The format of the IR debugging instrumentation:                     
                                                                                    - 'console': The tensors are dumped in text format in the console.  
                                                                                    - 'bin': The tensors are dumped in binary format in separate files. 
                                                                                             Each file will contain the tensor type and tensor data.    
                                                                                    - 'txt': The tensors are dumped in text format in separate files.   
                                                                                             Each file will contain the tensor type and tensor data.    
                                                                                    - 'rawbin': The tensors are dumped in raw binary format in separate 
                                                                                                files. Each file will contain ONLY the tensor data.     
                                                                                    - 'rawtxt': The tensors are dumped in raw text format in separate   
                                                                                                files. Each file will contain ONLY the tensor data.
  -instrument-debug-only=<string>                                                 - Instrument the IR for debugging, but only the listed instructions
  -instrument-ir                                                                  - Instrument the IR instructions
  -instrument-ir-only=<string>                                                    - Instrument the IR but only the listed instructions names
  -optimize-ir                                                                    - Enable IR optimizations

Loader Options:

  -assert-all-nodes-quantized                                                     - Debugging tool, used to assert the quantizer quantizes all nodes in the model, or abort otherwise. When false, nodes that are unsupported as quantized by the backend will be left unquantized, and may have their inputs dequantized/outputs quantized as necessary. Can be used in conjunction with -keep-original-precision-for-nodes to explicitly whitelist node kinds that are allowed to be left unquantized.
  -backend=<string>                                                               - Backend to use, e.g., Interpreter, CPU, OpenCL:
  -calibrate-constants                                                            - Option to enable the quantization calibration for constant weights which is disabled by default.
  -convert-placeholders                                                           - Convert model placeholders by merging ConvertTo, Quantize and Dequantize nodes into the model inputs and outputs.
  -convert-to-fp16                                                                - Run all floating-point computation in fp16.
  -do-not-lower-nodes-for-profiling=<NodeNames (e.g. Convolution,FullyConnected)> - Use to specify the name of nodes (e.g. Convolution, FullyConnected, etc.) that should not be lowered during profiling. All nodes of the listed kinds will be kept as is; e.g. if Conv is specified and the model has group convolutions then the convolution will not be lowered for profiling. This means when using the profile for quantization, the node should not be lowered then either.
  -dump-profile=<profile.yaml>                                                    - Perform quantization profiling for a given graph and dump result to the file.
  -emit-bundle=<string>                                                           - Output directory for the bundle serialization
  -enable-channelwise                                                             - Enable channelwise quantized Convolution.
  -enable-rowwise                                                                 - Enable rowwise quantized FullyConnected.
  -fp16-format                                                                    - fp16 format to use.
    =fp16                                                                         -   Use fp16
    =bfloat16                                                                     -   Use bfloat16
  -iterations=<uint>                                                              - Number of iterations to perform
  -keep-original-precision-for-nodes=<NodeNames (e.g. Add,Div)>                   - Use to specify the name of nodes (e.g. Add, Div, etc.) that should be kept as is when conversion/quantization is requested. All nodes of the listed kinds will be kept as is;e.g. if Add is specified and there are multiple Add nodes in the input loaded model, none would be quantized/converted.
  -load-profile=<profile.yaml>                                                    - Load quantization profile file and quantize the graph
  -main-entry-name=<string>                                                       - Name of the main entry in the bundle. This name is used as the function name of the entry point to the network.
  -model=<modelPath>                                                              - Specify one of three:
                                                                                    1. Path to ONNX model file.
                                                                                    2. Two paths to Caffe2 model files: network structure and weight.
                                                                                    3. Path to directory with the Caffe2 network structure <predict_net.pb> and weight <init_net.pb> files.
  -model-input=<name,[type,[scale,offset],shape]>                                 -  For ONNX models the inputs of the graph can be inferred   
                                                                                     automatically and hence this option is not mandatory.     
                                                                                     For Caffe2 models the graph definition does not contain   
                                                                                     the description of the inputs and hence must be provided  
                                                                                     explicitly using this option. One or more model inputs    
                                                                                     are provided using the following format:                  
                                                                                        -model-input=<inputName1>,<inputType1>,<inputShape1>   
                                                                                        -model-input=<inputName2>,<inputType2>,<inputShape2>   
                                                                                        ....................................................   
                                                                                     For quantized types the format is slightly different since
                                                                                     the scale and offset parameters should also be provided:  
                                                                                        -model-input=<name>,<type>,<scale>,<offset>,<shape>    
                                                                                     For example we can can provide one or more inputs:        
                                                                                        -model-input=input_03_data,float,[1]                   
                                                                                        -model-input=data_bias,int32,[1,32,32]                 
                                                                                        -model-input=data,int8q,0.123,-13,[1,10]               
                                                                                     If only the name is provided, the default type is 'float' 
                                                                                     and the default shape is '[1]':                           
                                                                                        -model-input=<inputName1>                              
                                                                                     The supported types are:                                  
                                                                                        - float, float16 (floating point types)                
                                                                                        - int32, int64 (integer types)                         
                                                                                        - int8q, int16q, int32q (integer quantized types)      
                                                                                        - bool (logic type)
  -network-name=<string>                                                          - Name of the network being bundled. This name is used as a prefix for all the files that are generated.
  -num-devices=<N>                                                                - Number of Devices to use
  -num-histogram-bins=<N>                                                         - Number of bins used for histogram during profiling. If histogram based calibration is used then the number of histogram bins must be greater than 255 in order for any calibration to take place (in the order of 1000's).
  -quantization-calibration                                                       - Specify which quantization calibration method to use
    =none                                                                         -   No calibration
    =KL                                                                           -   Quantization calibration method based on minimizing the Kullback-Leibler divergence metric (relative entropy)
  -quantization-precision                                                         - Specify which quantization precision to use, e.g., Int8
    =Int8                                                                         -   Use Int8 quantization
    =Int16                                                                        -   Use Int16 quantization
  -quantization-precision-bias                                                    - Specify which quantization precision to use for bias of Convolution and Fully Connected nodes.
    =Int8                                                                         -   Use Int8 bias quantization
    =Int16                                                                        -   Use Int16 bias quantization
    =Int32                                                                        -   Use Int32 bias quantization
  -quantization-schema                                                            - Specify which quantization schema to use
    =asymmetric                                                                   -   Use asymmetric ranges
    =symmetric                                                                    -   Use symmetric ranges
    =symmetric_with_uint8                                                         -   Use symmetric ranges with potentially uint8 ranges
    =symmetric_with_power2_scale                                                  -   Use symmetric ranges with power of 2 scaling factor
  -run-all-inputs-on-all-devices                                                  - Run all inputs on all devices. Used for testing purposes.
  -time                                                                           - Print timer output to stderr detailing how long it takes for the program to execute
  -verbose                                                                        - Specify whether to run with verbose output

Model Loader Options:

  -const-fold-ops                                                                 - Performs constant folding on ONNX and Caffe Operators while loading.

ONNX Model Loader Options:

  -loop-unroll-limit=<uint>                                                       - Maximum unrollable iterations for the Loop operator
  -onnx-define-symbol=<name,value>                                                - Define (replace) the undefined symbols from the tensor descriptions
                                                                                    in the ONNX model with actual integer sizes. The undefined symbols 
                                                                                    are marked in the proto description with the 'dim_param' field. For
                                                                                    example, if the model contains a tensor with the size described as 
                                                                                    'None' x 3 x 224 x 224, the symbol 'None' can be replaced with an  
                                                                                    actual integer size (for example 1) by using the following command 
                                                                                    line option:                                                       
                                                                                        -onnx-define-symbol=None,1                                     
                                                                                    Multiple symbols can be defined using this option, for example:    
                                                                                        -onnx-define-symbol=<symbol_name1>,<symbol_value1>             
                                                                                        -onnx-define-symbol=<symbol_name2>,<symbol_value2>             
                                                                                        ..................................................
  -onnx-export-rnn-states                                                         - Option to export the states of the ONNX RNN operators (for example 
                                                                                    RNN, GRU, LSTM) as graph placeholders regardless of whether the    
                                                                                    states are explicitly set or not in the graph. The placeholders are
                                                                                    also providing an automatic way for tracking the RNN states since  
                                                                                    the states are updated automatically with the new RNN states after 
                                                                                    each inference. Default is false.

TensorFlowLite Model Loader Options:

  -tflite-bias-scale-check-max-error=<number>                                     - TensorFlowLite mandates that for quantized operators like Conv2D the bias quantization parameter biasScale = inputScale * weightsScale but some pre-quantized models do not EXACTLY satisfy this relation but with very small relative errors (around 1e-8). Hence we allow a tolerance of 1e-6 which, if satisfied, then we adjust the bias to conform to the restriction.
  -tflite-bias-scale-check-throw-error                                            - TensorFlowLite mandates that for quantized operators like Conv2D the bias quantization parameter biasScale = inputScale * weightsScale. If this contraint is not met within the given tolerance then an error will be thrown if this option is enabled.
  -tflite-float-inputs                                                            - TensorFlowLite loader option to replace the quantized inputs with floating point inputs.
  -tflite-float-outputs                                                           - TensorFlowLite loader option to replace the quantized outputs with floating point outputs.
  -tflite-float-softmax                                                           - TensorFlowLite loader option to replace a quantized Softmaxwith a floating point Softmax.
  -tflite-uint8-to-int8                                                           - TensorFlowLite loader option to convert the model from UINT8 data type to INT8 data type.

graph Pass Manager Options:

  -dump-graph-after-all-passes                                                    - Debug option to dump the IR after all passes.
  -dump-graph-after-passes=<Comma separated pass names (e.g. DSE, DCE)>           - Debug option to dump the IR after listed passes.
  -dump-graph-before-all-passes                                                   - Debug option to dump the IR before all passes.
  -dump-graph-before-passes=<Comma separated pass names (e.g. DSE, DCE)>          - Debug option to dump the IR before the listed passes.
  -print-graph-passes                                                             - Print all of the passes run by the pass manager.
  -stop-graph-passes-after-num=<uint>                                             - Number of passes to run before preventing running any passes. Used for debugging.
  -verify-after-all-graph-passes                                                  - Verify the IR after all passes.
  -verify-after-graph-passes=<Comma separated pass names (e.g. DSE, DCE)>         - Verify the IR after the listed passes.
  -verify-before-all-graph-passes                                                 - Verify the IR before all passes.
  -verify-before-graph-passes=<Comma separated pass names (e.g. DSE, DCE)>        - Verify the IR before the listed passes.

ir Pass Manager Options:

  -dump-ir-after-all-passes                                                       - Debug option to dump the IR after all passes.
  -dump-ir-after-passes=<Comma separated pass names (e.g. DSE, DCE)>              - Debug option to dump the IR after listed passes.
  -dump-ir-before-all-passes                                                      - Debug option to dump the IR before all passes.
  -dump-ir-before-passes=<Comma separated pass names (e.g. DSE, DCE)>             - Debug option to dump the IR before the listed passes.
  -print-ir-passes                                                                - Print all of the passes run by the pass manager.
  -stop-ir-passes-after-num=<uint>                                                - Number of passes to run before preventing running any passes. Used for debugging.
  -verify-after-all-ir-passes                                                     - Verify the IR after all passes.
  -verify-after-ir-passes=<Comma separated pass names (e.g. DSE, DCE)>            - Verify the IR after the listed passes.
  -verify-before-all-ir-passes                                                    - Verify the IR before all passes.
  -verify-before-ir-passes=<Comma separated pass names (e.g. DSE, DCE)>           - Verify the IR before the listed passes.
