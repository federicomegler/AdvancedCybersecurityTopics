import claripy

mt = [0] * 624

def m_seedRand(seed):
	global index
	global mt
	buffer[0] = seed & 0xffffffff;
	buffer[0x4e0] = 1;
	while (index < 0x270)
		mt[index] = (mt[index-1] * 0x17b5) & 0xffffffff
		index = index + 1
	return

print(m_seedRand(mt))

seed = claripy.BVS("seed" , 32)



def genRandLong(mt):
	global mt
	global index
	
	if (0x26f < index) || (index < 0):
		if (0x270 < index) || (index < 0):
			m_seedRand(,0x1105);
    }
    index = 0;
    while (index < 0xe3) {
      uVar3 = (uint)state->mt[index + 1];
      state->mt[index] =
           state->mt[index + 0x18d] ^
           (ulong)((uVar3 & 0x7fffffff | (uint)state->mt[index] & 0x80000000) >> 1) ^
           *(ulong *)(mag.3808 + (ulong)(uVar3 & 1) * 8);
      index = index + 1;
    }
    while (index < 0x26f) {
      uVar3 = (uint)state->mt[index + 1];
      state->mt[index] =
           state->mt[index + -0xe3] ^
           (ulong)((uVar3 & 0x7fffffff | (uint)state->mt[index] & 0x80000000) >> 1) ^
           *(ulong *)(mag.3808 + (ulong)(uVar3 & 1) * 8);
      index = index + 1;
    }
    uVar3 = (uint)state->mt[0];
    state->mt[0x26f] =
         state->mt[0x18c] ^ (ulong)((uVar3 & 0x7fffffff | (uint)state->mt[0x26f] & 0x80000000) >> 1)
         ^ *(ulong *)(mag.3808 + (ulong)(uVar3 & 1) * 8);
    state->index = 0;
  }
  iVar1 = state->index;
  state->index = iVar1 + 1;
  uVar2 = state->mt[iVar1] ^ state->mt[iVar1] >> 0xb;
  uVar2 = uVar2 ^ (uint)(uVar2 << 7) & 0x9d2c5680;
  uVar2 = uVar2 ^ (uint)(uVar2 << 0xf) & 0xefc60000;
  return uVar2 ^ uVar2 >> 0x12;
}