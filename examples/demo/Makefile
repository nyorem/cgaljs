CXX=em++
ROOT=/home/nyorem/projets/web/cgaljs
LIBDIR=$(ROOT)/libs
INCDIR=$(ROOT)/includes

INCS=-I$(INCDIR)/geogram -I$(INCDIR)/dgtal -I$(INCDIR)
LIBS= $(LIBDIR)/libgeogram.a $(LIBDIR)/libgeogram_gfx.a $(LIBDIR)/libDGtal.a

ESFLAGS  = -std=c++11 $(INCS)
ESFLAGS += -O2
LDFLAGS=-s WASM=0 \
	-s USE_GLFW=3 \
	-s FORCE_FILESYSTEM=1 \
	-s TOTAL_MEMORY=268435456 \
	-s EXPORTED_FUNCTIONS='["_main","_file_system_changed_callback"]' \
	-s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall"]' \
	$(LIBS)

EXE=main
OBJECTS=$(EXE).o

all: main.html

%.o: %.cpp
	$(CXX) $(ESFLAGS) -c $< -o $@

$(EXE).html: $(OBJECTS)
	$(CXX)  $(LDFLAGS) $^ -o $@

run: $(EXE).html
	python3 -m http.server

clean:
	@rm -fv *.o

proper: clean
	@rm -fv $(EXE).js
	@rm -fv $(EXE).html
