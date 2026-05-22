# ===== Compiler =====
CC      := cc
AR      := ar
CFLAGS  := -std=c99 -Wall -Wextra -O2 -fPIC

# ===== Directories =====
QBE_DIR   := qbe
WRAP_DIR  := wrapper
BUILD_DIR := build

# ===== Output =====
LIB_DIR := lib

STATIC_LIB := $(LIB_DIR)/libpyqbe.a
SHARED_LIB := $(LIB_DIR)/libpyqbe.so


# ===== QBE Sources =====

COMMOBJ = \
	 util.o parse.o abi.o cfg.o mem.o ssa.o alias.o \
	load.o copy.o fold.o gvn.o gcm.o simpl.o ifopt.o \
	live.o spill.o rega.o emit.o

AMD64OBJ = \
	amd64/targ.o amd64/sysv.o amd64/isel.o \
	amd64/emit.o amd64/winabi.o

ARM64OBJ = \
	arm64/targ.o arm64/abi.o arm64/isel.o \
	arm64/emit.o

RV64OBJ = \
	rv64/targ.o rv64/abi.o rv64/isel.o \
	rv64/emit.o

QBE_OBJ_REL := $(COMMOBJ) $(AMD64OBJ) $(ARM64OBJ) $(RV64OBJ)

# prepend qbe/
QBE_SRC := $(addprefix $(QBE_DIR)/,$(QBE_OBJ_REL:.o=.c))

# ===== Wrapper =====
WRAP_SRC := $(WRAP_DIR)/qbe_api.c

SRC := $(WRAP_SRC) $(QBE_SRC)

# ===== Objects =====
OBJ := $(patsubst %.c,$(BUILD_DIR)/%.o,$(SRC))

# ===== Includes =====
INCLUDES := -I$(QBE_DIR)

# ===== Default =====
all: static shared

# ===== config.h =====
$(QBE_DIR)/config.h:
	cd $(QBE_DIR) && $(MAKE) config.h

# ===== Compile =====
$(BUILD_DIR)/%.o: %.c $(QBE_DIR)/config.h
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

# ===== Static =====
static: $(OBJ)
	@mkdir -p $(LIB_DIR)
	$(AR) rcs $(STATIC_LIB) $(OBJ)

# ===== Shared =====
shared: $(OBJ)
	@mkdir -p $(LIB_DIR)
	$(CC) -shared -o $(SHARED_LIB) $(OBJ)

# ===== Clean =====
clean:
	rm -rf $(BUILD_DIR)
	rm -rf $(LIB_DIR)
	cd $(QBE_DIR) && $(MAKE) clean-gen

# ===== Rebuild =====
rebuild: clean all

.PHONY: all static shared clean rebuild