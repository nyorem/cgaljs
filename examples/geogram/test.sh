em++ main.cpp \
    # -O3 \
    -s WASM=0 \
    -s USE_GLFW=3 \
    -s FORCE_FILESYSTEM=1 \
    -s TOTAL_MEMORY=268435456 \
    -s EXPORTED_FUNCTIONS='["_main","_file_system_changed_callback"]' \
    -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall"]' \
    ../../libs/libgeogram.a \
    ../../libs/libgeogram_gfx.a \
    -I ../../includes/geogram \
    -o main.html

# python3 -m http.server
