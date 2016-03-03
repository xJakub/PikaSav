"""
Created on 26/06/2011

@author: Ritchie
"""

class RSSav:

    def __init__(self, file, repair = False):
        self.firsttime = True
        self.version = 'Ruby/Sapphire'
        self.ok = repair
        self.repair = repair
        self.maps = []
        table = [''] * 256
        etable = [''] * 256
        table[0] = ' '
        table[1] = 'HERO'
        table[27] = '\xe9'
        table[45] = '&'
        table[92] = '('
        table[93] = ')'
        table[121] = '-UP'
        table[122] = '-DOWN'
        table[123] = '-LEFT'
        table[124] = '-RIGHT'
        table[171] = '!'
        table[172] = '?'
        table[173] = '.'
        table[174] = '-'
        table[176] = '..'
        table[177] = '"'
        table[178] = '"2'
        table[179] = "'2"
        table[180] = "'"
        table[181] = 'mA'
        table[182] = 'fE'
        table[183] = '$'
        table[184] = ','
        table[185] = 'x-'
        table[186] = '/'
        for x in range(26):
            table[187 + x] = chr(65 + x)
            table[213 + x] = chr(97 + x)

        for x in range(10):
            table[161 + x] = str(x)

        table[240] = ':'
        table[250] = '='
        table[251] = '*'
        table[252] = '=2'
        table[253] = '@'
        table[254] = '+'
        self.dtable = table
        for x in range(256):
            if len(table[x]) == 1:
                etable[ord(table[x])] = chr(x)

        self.etable = etable
        self.file = file
        self.refreshfile()

    def refreshfile(self):
        fb = open(self.file, 'rb')
        self.buffer = fb.read()
        self.obuffer = self.buffer[:]
        fb.close()
        if self.repair == False:
            if len(self.buffer) < 131072 or len(self.buffer) > 262144:
                self.file = None
                self.buffer = ''
                return
        self.refresh()

    def saveas(self, file):
        self.repair = self.ok
        self.pack_sav()
        self.check_sav()
        fb = open(file, 'wb')
        fb.write(self.buffer)
        fb.close()

    def save(self):
        self.repair = self.ok
        self.pack_sav()
        self.saveas(self.file)

    def refresh(self):
        if not self.firsttime:
            self.pack_sav()
        self.firsttime = False
        self.check_sav()
        if self.ok == False:
            return False
        self.unpack_sav()
        self.load_money()
        self.load_names()
        self.load_badges()
        self.load_items()
        self.load_pokedex()
        self.load_options()
        self.load_time()
        self.load_pokemon()

    def unpack_sav(self):
        self.gbuffer = ''
        for b in range(14):
            self.gbuffer += self.gbuffers[b]

        if ord(self.gbuffer[18899]) == 0:
            self.flok = False
        else:
            self.rsok = False
        if not self.repair:
            self.ok = self.rsok

    def pack_sav(self):
        newbuffer = self.buffer
        for b in range(14):
            start = self.boffset[b]
            self.gbuffers[b] = self.gbuffer[3968 * b:3968 * b + 3968]
            self.buffer = self.buffer[0:start] + self.gbuffers[b] + self.buffer[start + 3968:]

    def check_sav(self):
        FLtable = (3876, 3968, 3968, 3968, 3776, 3968, 3968, 3968, 3968, 3968, 3968, 3968, 3968, 2000, 28, 256)
        RStable = (2192, 3968, 3968, 3968, 3136, 3968, 3968, 3968, 3968, 3968, 3968, 3968, 3968, 2000, 3968, 3968)
        self.gbuffers = ['',
         '',
         '',
         '',
         '',
         '',
         '',
         '',
         '',
         '',
         '',
         '',
         '',
         '']
        self.buffers = ''
        self.gsaveid = [-1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1]
        self.boffset = [-1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1,
         -1]
        self.ok = False
        self.rsok = True
        self.flok = False
        for block in range(28):
            start = 4096 * block
            blockid = ord(self.buffer[start + 4084])
            saveid = ord(self.buffer[start + 4092])
            saveid += ord(self.buffer[start + 4093]) << 8
            saveid += ord(self.buffer[start + 4094]) << 16
            saveid += ord(self.buffer[start + 4095]) << 24
            size = 3968
            rssize = RStable[blockid]
            flsize = FLtable[blockid]
            rschecksum = 0
            flchecksum = 0
            self.checksum = ord(self.buffer[start + 4086]) + ord(self.buffer[start + 4087]) * 256
            if self.gsaveid[blockid] < saveid:
                self.gbuffers[blockid] = self.buffer[start:start + 3968]
                self.gsaveid[blockid] = saveid
                self.boffset[blockid] = start
                for x in range(0, rssize, 4):
                    rschecksum += ord(self.buffer[x + start])
                    rschecksum += ord(self.buffer[x + start + 1]) << 8
                    rschecksum += ord(self.buffer[x + start + 2]) << 16
                    rschecksum += ord(self.buffer[x + start + 3]) << 24

                rschecksum += rschecksum >> 16
                rschecksum &= 65535
                flchecksum += flchecksum >> 16
                flchecksum &= 65535
                if self.firsttime == True:
                    if self.repair == False:
                        if flchecksum != self.checksum:
                            self.flok = False
                        if rschecksum != self.checksum:
                            self.rsok = False
                if self.rsok == False and self.repair == False:
                    self.ok = False
                self.checksum = rschecksum
                self.setbyte(start + 4086, rschecksum & 255)
                self.setbyte(start + 4087, rschecksum >> 8 & 255)

        if self.rsok:
            self.ok += 1
        if self.flok:
            self.ok += 2

    def set(self, var, value):
        if var == 'name':
            value = self.encode(value, 7)
            self.gbuffer = value + chr(80) + self.buffer[8:]
        if var == 'money':
            self.gbuffer = self.setbyte(5136, int(value) & 255, self.gbuffer)
            self.gbuffer = self.setbyte(5137, int(value) >> 8 & 255, self.gbuffer)
            self.gbuffer = self.setbyte(5138, int(value) >> 16 & 255, self.gbuffer)
        if var == 'chips':
            self.gbuffer = self.setbyte(5140, int(value) & 255, self.gbuffer)
            self.gbuffer = self.setbyte(5141, int(value) >> 8 & 255, self.gbuffer)
        if var == 'hours':
            self.gbuffer = self.setbyte(14, int(value) & 255, self.gbuffer)
            self.gbuffer = self.setbyte(15, int(value) >> 8 & 255, self.gbuffer)
        if var == 'minutes':
            self.gbuffer = self.setbyte(16, int(value) & 255, self.gbuffer)
        if var == 'seconds':
            self.gbuffer = self.setbyte(17, int(value) & 255, self.gbuffer)

    def setbyte(self, byte, value, string = None):
        if string == None:
            self.buffer = self.buffer[0:byte] + chr(value) + self.buffer[byte + 1:]
        else:
            return string[0:byte] + chr(value) + string[byte + 1:]

    def load_time(self):
        self.hours = ord(self.gbuffer[14])
        self.hours += ord(self.gbuffer[15]) * 256
        self.minutes = ord(self.gbuffer[16])
        self.seconds = ord(self.gbuffer[17])

    def load_options(self):
        return
        options = ord(self.buffer[9729])
        self.animation = not options >> 7
        self.mantain = options >> 6 & 1
        self.textspeed = options & 15

    def setpokedex(self, x, isseen, iscatched):
        pos = 2 ** ((x - 1) % 8)
        seen = ord(self.gbuffer[6328 + (x - 1) // 8])
        catched = ord(self.gbuffer[40 + (x - 1) // 8])
        if self.seen[x] != isseen:
            seen ^= pos
        if self.catched[x] != iscatched:
            catched ^= pos
        self.gbuffer = self.setbyte(92 + (x - 1) // 8, seen, self.gbuffer)
        self.gbuffer = self.setbyte(6328 + (x - 1) // 8, seen, self.gbuffer)
        self.gbuffer = self.setbyte(18956 + (x - 1) // 8, seen, self.gbuffer)
        self.gbuffer = self.setbyte(40 + (x - 1) // 8, catched, self.gbuffer)

    def load_pokedex(self):
        self.seen = [0] * 393
        self.catched = [0] * 393
        for x in range(49):
            catched = ord(self.gbuffer[40 + x])
            seen = ord(self.gbuffer[92 + x])
            for y in range(8):
                self.catched[x * 8 + y + 1] = catched >> y & 1
                self.seen[x * 8 + y + 1] = seen >> y & 1

    def load_badges(self):
        return
        badgesmap = ord(self.buffer[9730])
        self.badges = [0] * 8
        for x in range(8):
            self.badges[x] = badgesmap >> x & 1

    def load_items(self):
        items = [[0, 0]] * 163
        for x in range(163):
            item = ord(self.gbuffer[5344 + 4 * x]) + ord(self.gbuffer[5345 + 4 * x]) * 256
            count = ord(self.gbuffer[5346 + 4 * x]) + ord(self.gbuffer[5347 + 4 * x]) * 256
            items[x] = [item, count]

        self.items = items
        self.itemcount = 0
        pcitems = [[0, 0]] * 50
        for x in range(50):
            item = ord(self.gbuffer[5144 + 4 * x]) + ord(self.gbuffer[5145 + 4 * x]) * 256
            count = ord(self.gbuffer[5146 + 4 * x]) + ord(self.gbuffer[5147 + 4 * x]) * 256
            pcitems[x] = [item, count]

        self.pcitems = pcitems
        self.pcitemcount = ord(self.buffer[9343])

    def load_pokemon(self):
        self.pokemon = [''] * 6
        self.pcpokemon = [''] * 420
        self.pokemoncount = 6
        self.boxpokemoncount = [0] * 30
        self.boxoffset = [0] * 30
        for p in range(6):
            self.pokemon[p] = self.gbuffer[4536 + 100 * p:4536 + 100 * (p + 1)]

        self.currentbox = ord(self.gbuffer[19840]) & 127
        for b in range(14):
            offset = 19844 + 2400 * b
            self.boxoffset[b] = offset
            self.boxpokemoncount[b] = 0
            for p in range(30):
                self.pcpokemon[30 * b + p] = self.gbuffer[offset + 80 * p:offset + 80 * (p + 1)]
                if self.pkm_get(self.pcpokemon[30 * b + p], 'num'):
                    self.boxpokemoncount[b] += 1

    def setpokemon(self, p, pkm):
        self.gbuffer = self.gbuffer[0:4536 + 100 * p] + pkm + self.gbuffer[4536 + 100 * (p + 1):]

    def setpcpokemon(self, p, pkm):
        self.gbuffer = self.gbuffer[0:19844 + 80 * p] + pkm + self.gbuffer[19844 + 80 * (p + 1):]

    def pkm_getdata(self, pkm):
        blockpos = [(0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3),
         (1, 1, 2, 3, 2, 3, 0, 0, 0, 0, 0, 0, 2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2),
         (2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2, 0, 0, 0, 0, 0, 0, 3, 2, 3, 2, 1, 1),
         (3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0)]
        pid = ord(pkm[0]) + (ord(pkm[1]) << 8) + (ord(pkm[2]) << 16) + (ord(pkm[3]) << 24)
        tid = ord(pkm[4]) + (ord(pkm[5]) << 8) + (ord(pkm[6]) << 16) + (ord(pkm[7]) << 24)
        key = pid ^ tid
        keys = [0] * 4
        if sum:
            for k in range(4):
                keys[k] = key >> k * 8 & 255

        order = pid % 24
        data = pkm[32:80]
        decdata = ''
        for block in range(4):
            for byte in range(12):
                pos = blockpos[block][order] * 12 + byte
                enc = ord(data[pos])
                key = keys[byte % 4]
                decdata += chr(enc ^ key)

        return decdata

    def pkm_setdata(self, pkm, data):
        blockpos = [(0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3),
         (1, 1, 2, 3, 2, 3, 0, 0, 0, 0, 0, 0, 2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2),
         (2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2, 0, 0, 0, 0, 0, 0, 3, 2, 3, 2, 1, 1),
         (3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0)]
        pid = ord(pkm[0]) + (ord(pkm[1]) << 8) + (ord(pkm[2]) << 16) + (ord(pkm[3]) << 24)
        tid = ord(pkm[4]) + (ord(pkm[5]) << 8) + (ord(pkm[6]) << 16) + (ord(pkm[7]) << 24)
        key = pid ^ tid
        keys = [0] * 4
        for k in range(4):
            keys[k] = key >> k * 8 & 255

        order = pid % 24
        for block in range(4):
            for byte in range(12):
                pos = blockpos[block][order] * 12 + byte + 32
                dec = ord(data[block * 12 + byte])
                key = keys[byte % 4]
                pkm = self.setbyte(pos, dec ^ key, pkm)

        sum = 0
        for i in range(12):
            for k in range(2):
                sum += ord(pkm[32 + k * 2 + i * 4]) ^ keys[k * 2]
                sum += (ord(pkm[33 + k * 2 + i * 4]) ^ keys[k * 2 + 1]) * 256

        pkm = self.setbyte(28, sum & 255, pkm)
        pkm = self.setbyte(29, sum >> 8 & 255, pkm)
        return pkm

    def pkm_sget(self, pkm, block, byte):
        blockpos = [(0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3),
         (1, 1, 2, 3, 2, 3, 0, 0, 0, 0, 0, 0, 2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2),
         (2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2, 0, 0, 0, 0, 0, 0, 3, 2, 3, 2, 1, 1),
         (3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0)]
        pid = ord(pkm[0]) + (ord(pkm[1]) << 8) + (ord(pkm[2]) << 16) + (ord(pkm[3]) << 24)
        tid = ord(pkm[4]) + (ord(pkm[5]) << 8) + (ord(pkm[6]) << 16) + (ord(pkm[7]) << 24)
        key = pid ^ tid
        data = pkm[32:80]
        order = pid % 24
        pos = blockpos[block][order] * 12 + byte
        enc = ord(data[pos])
        byte = byte % 4
        key = key >> byte * 8 & 255
        return enc ^ key

    def pkm_sset(self, pkm, block, byte, value, sum = True):
        blockpos = [(0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3),
         (1, 1, 2, 3, 2, 3, 0, 0, 0, 0, 0, 0, 2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2),
         (2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2, 0, 0, 0, 0, 0, 0, 3, 2, 3, 2, 1, 1),
         (3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0)]
        pid = ord(pkm[0]) + (ord(pkm[1]) << 8) + (ord(pkm[2]) << 16) + (ord(pkm[3]) << 24)
        tid = ord(pkm[4]) + (ord(pkm[5]) << 8) + (ord(pkm[6]) << 16) + (ord(pkm[7]) << 24)
        key = pid ^ tid
        order = pid % 24
        pos = blockpos[block][order] * 12 + byte + 32
        byte = byte % 4
        keys = [0] * 4
        if sum:
            for k in range(4):
                keys[k] = key >> k * 8 & 255

        key = key >> byte * 8 & 255
        pkm = self.setbyte(pos, value ^ key, pkm)
        if sum:
            sum = 0
            for i in range(12):
                for k in range(2):
                    sum += ord(pkm[32 + k * 2 + i * 4]) ^ keys[k * 2]
                    sum += (ord(pkm[33 + k * 2 + i * 4]) ^ keys[k * 2 + 1]) * 256

            pkm = self.setbyte(28, sum & 255, pkm)
            pkm = self.setbyte(29, sum >> 8 & 255, pkm)
        return pkm

    def pkm_ssetw(self, pkm, block, byte, value, sum = True):
        pkm = self.pkm_sset(pkm, block, byte, value & 255, False)
        pkm = self.pkm_sset(pkm, block, byte + 1, value >> 8 & 255, sum)
        return pkm

    def pkm_ssetdw(self, pkm, block, byte, value):
        pkm = self.pkm_ssetw(pkm, block, byte, value & 65535, False)
        pkm = self.pkm_ssetw(pkm, block, byte + 2, value >> 16 & 65535)
        return pkm

    def pkm_sgetw(self, pkm, block, byte):
        return self.pkm_sget(pkm, block, byte) + self.pkm_sget(pkm, block, byte + 1) * 256

    def pkm_sgetdw(self, pkm, block, byte):
        return self.pkm_sgetw(pkm, block, byte) + self.pkm_sgetw(pkm, block, byte + 2) * 65536

    def pkm_get(self, pkm, var):
        if var == 'sprite':
            return self.pkm_sgetw(pkm, 0, 0)
        if var == 'num':
            return self.pkm_sgetw(pkm, 0, 0)
        if var == 'pid':
            return ord(pkm[0]) + (ord(pkm[1]) << 8) + (ord(pkm[2]) << 16) + (ord(pkm[3]) << 24)
        if var == 'otname':
            return self.decode(pkm[20:27])
        if var == 'name':
            return self.decode(pkm[8:18])
        if var == 'hp':
            return ord(pkm[86]) + ord(pkm[87]) * 256
        if var == 'level' or var == 'curlevel':
            return ord(pkm[84])
        if var == 'asleep':
            if ord(pkm[80]) & 7:
                return True
            return False
        if var == 'poisoned':
            if ord(pkm[80]) & 8:
                return True
            return False
        if var == 'burned':
            if ord(pkm[80]) & 16:
                return True
            return False
        if var == 'frozen':
            if ord(pkm[80]) & 32:
                return True
            return False
        if var == 'paralyzed':
            if ord(pkm[80]) & 64:
                return True
            return False
        if var == 'ok':
            if ord(pkm[80]) & 127:
                return False
            return True
        if var == 'catchrate' or var == 'item':
            return self.pkm_sgetw(pkm, 0, 2)
        if var == 'move1':
            return self.pkm_sgetw(pkm, 1, 0)
        if var == 'move2':
            return self.pkm_sgetw(pkm, 1, 2)
        if var == 'move3':
            return self.pkm_sgetw(pkm, 1, 4)
        if var == 'move4':
            return self.pkm_sgetw(pkm, 1, 6)
        if var == 'otnum':
            return ord(pkm[4]) + (ord(pkm[5]) << 8)
        if var == 'secretid':
            return ord(pkm[6]) + (ord(pkm[7]) << 8)
        if var == 'exp':
            return self.pkm_sgetdw(pkm, 0, 4)
        if var == 'maxhpev':
            return self.pkm_sget(pkm, 2, 0)
        if var == 'attackev':
            return self.pkm_sget(pkm, 2, 1)
        if var == 'defenseev':
            return self.pkm_sget(pkm, 2, 2)
        if var == 'speedev':
            return self.pkm_sget(pkm, 2, 3)
        if var == 'specialattackev':
            return self.pkm_sget(pkm, 2, 4)
        if var == 'specialdefenseev':
            return self.pkm_sget(pkm, 2, 5)
        if var == 'coolness':
            return self.pkm_sget(pkm, 2, 6)
        if var == 'beauty':
            return self.pkm_sget(pkm, 2, 7)
        if var == 'cuteness':
            return self.pkm_sget(pkm, 2, 8)
        if var == 'smartness':
            return self.pkm_sget(pkm, 2, 9)
        if var == 'toughness':
            return self.pkm_sget(pkm, 2, 10)
        if var == 'feel':
            return self.pkm_sget(pkm, 2, 11)
        if var == 'maxhpiv':
            return self.pkm_sgetdw(pkm, 3, 4) & 31
        if var == 'attackiv':
            return self.pkm_sgetdw(pkm, 3, 4) >> 5 & 31
        if var == 'defenseiv':
            return self.pkm_sgetdw(pkm, 3, 4) >> 10 & 31
        if var == 'speediv':
            return self.pkm_sgetdw(pkm, 3, 4) >> 15 & 31
        if var == 'specialattackiv':
            return self.pkm_sgetdw(pkm, 3, 4) >> 20 & 31
        if var == 'specialdefenseiv':
            return self.pkm_sgetdw(pkm, 3, 4) >> 25 & 31
        if var == 'move1pp':
            return self.pkm_sget(pkm, 1, 8)
        if var == 'move1ppup':
            return self.pkm_sget(pkm, 0, 8) & 3
        if var == 'move2pp':
            return self.pkm_sget(pkm, 1, 9)
        if var == 'move2ppup':
            return self.pkm_sget(pkm, 0, 8) >> 2 & 3
        if var == 'move3pp':
            return self.pkm_sget(pkm, 1, 10)
        if var == 'move3ppup':
            return self.pkm_sget(pkm, 0, 8) >> 4 & 3
        if var == 'move4pp':
            return self.pkm_sget(pkm, 1, 11)
        if var == 'move4ppup':
            return self.pkm_sget(pkm, 0, 8) >> 6 & 3
        if var == 'happiness':
            return self.pkm_sget(pkm, 0, 9)
        if var == 'pokerus':
            return self.pkm_sget(pkm, 3, 0)
        if var == 'caughtlocation':
            return self.pkm_sget(pkm, 3, 1)
        if var == 'caughtlevel':
            return self.pkm_sget(pkm, 3, 2)
        if var == 'caughtball':
            return self.pkm_sget(pkm, 3, 3) >> 3 & 15
        if var == 'otgender':
            return self.pkm_sget(pkm, 3, 3) >> 7
        if var == 'maxhp':
            return ord(pkm[88]) + ord(pkm[89]) * 256
        if var == 'attack':
            return ord(pkm[90]) + ord(pkm[91]) * 256
        if var == 'defense':
            return ord(pkm[92]) + ord(pkm[93]) * 256
        if var == 'speed':
            return ord(pkm[94]) + ord(pkm[95]) * 256
        if var == 'specialattack':
            return ord(pkm[96]) + ord(pkm[97]) * 256
        if var == 'specialdefense':
            return ord(pkm[98]) + ord(pkm[99]) * 256

    def pkm_set(self, pkm, var, value):
        if var == 'sprite':
            return self.pkm_ssetw(pkm, 0, 0, value)
        if var == 'num':
            return self.pkm_ssetw(pkm, 0, 0, value)
        if var == 'otname':
            if value != self.pkm_get(pkm, var):
                pkm = pkm[0:20] + self.encode(value, 7) + chr(80) + pkm[27:]
        if var == 'name':
            if value != self.pkm_get(pkm, var):
                pkm = pkm[0:8] + self.encode(value, 10) + chr(80) + pkm[18:]
        if var == 'hp':
            pkm = self.setbyte(86, value & 255, pkm)
            pkm = self.setbyte(87, value >> 8, pkm)
        if var == 'level':
            pkm = self.setbyte(84, value, pkm)
        if var == 'asleep':
            status = ord(pkm[80])
            if value:
                status |= 4
            else:
                status &= 248
            pkm = self.setbyte(80, status, pkm)
        if var == 'poisoned':
            status = ord(pkm[80])
            if value:
                status |= 8
            else:
                status &= 247
            pkm = self.setbyte(80, status, pkm)
        if var == 'burned':
            status = ord(pkm[80])
            if value:
                status |= 16
            else:
                status &= 239
            pkm = self.setbyte(80, status, pkm)
        if var == 'frozen':
            status = ord(pkm[80])
            if value:
                status |= 32
            else:
                status &= 223
            pkm = self.setbyte(80, status, pkm)
        if var == 'paralyzed':
            status = ord(pkm[80])
            if value:
                status |= 64
            else:
                status &= 191
            pkm = self.setbyte(80, status, pkm)
        if var == 'catchrate' or var == 'item':
            return self.pkm_ssetw(pkm, 0, 2, value)
        if var == 'move1':
            return self.pkm_ssetw(pkm, 1, 0, value)
        if var == 'move2':
            return self.pkm_ssetw(pkm, 1, 2, value)
        if var == 'move3':
            return self.pkm_ssetw(pkm, 1, 4, value)
        if var == 'move4':
            return self.pkm_ssetw(pkm, 1, 6, value)
        if var == 'otnum':
            data = self.pkm_getdata(pkm)
            pkm = self.setbyte(4, value & 255, pkm)
            pkm = self.setbyte(5, value >> 8, pkm)
            pkm = self.pkm_setdata(pkm, data)
        if var == 'secretid':
            data = self.pkm_getdata(pkm)
            pkm = self.setbyte(6, value & 255, pkm)
            pkm = self.setbyte(7, value >> 8, pkm)
            pkm = self.pkm_setdata(pkm, data)
        if var == 'pid':
            data = self.pkm_getdata(pkm)
            pkm = self.setbyte(0, value & 255, pkm)
            pkm = self.setbyte(1, value >> 8 & 255, pkm)
            pkm = self.setbyte(2, value >> 16 & 255, pkm)
            pkm = self.setbyte(3, value >> 24 & 255, pkm)
            pkm = self.pkm_setdata(pkm, data)
        if var == 'exp':
            return self.pkm_ssetdw(pkm, 0, 4, value)
        if var == 'maxhpev':
            return self.pkm_sset(pkm, 2, 0, value)
        if var == 'attackev':
            return self.pkm_sset(pkm, 2, 1, value)
        if var == 'defenseev':
            return self.pkm_sset(pkm, 2, 2, value)
        if var == 'speedev':
            return self.pkm_sset(pkm, 2, 3, value)
        if var == 'specialattackev':
            return self.pkm_sset(pkm, 2, 4, value)
        if var == 'specialdefenseev':
            return self.pkm_sset(pkm, 2, 5, value)
        if var == 'coolness':
            return self.pkm_sset(pkm, 2, 6, value)
        if var == 'beauty':
            return self.pkm_sset(pkm, 2, 7, value)
        if var == 'cuteness':
            return self.pkm_sset(pkm, 2, 8, value)
        if var == 'smartness':
            return self.pkm_sset(pkm, 2, 9, value)
        if var == 'toughness':
            return self.pkm_sset(pkm, 2, 10, value)
        if var == 'feel':
            return self.pkm_sset(pkm, 2, 11, value)
        if var == 'maxhpiv':
            ivs = (self.pkm_sgetdw(pkm, 3, 4) & 4294967295L - 31) + ((value & 31) << 0)
            return self.pkm_ssetdw(pkm, 3, 4, ivs)
        if var == 'attackiv':
            ivs = (self.pkm_sgetdw(pkm, 3, 4) & 4294967295L - 992) + ((value & 31) << 5)
            return self.pkm_ssetdw(pkm, 3, 4, ivs)
        if var == 'defenseiv':
            ivs = (self.pkm_sgetdw(pkm, 3, 4) & 4294967295L - 31744) + ((value & 31) << 10)
            return self.pkm_ssetdw(pkm, 3, 4, ivs)
        if var == 'speediv':
            ivs = (self.pkm_sgetdw(pkm, 3, 4) & 4294967295L - 1015808) + ((value & 31) << 15)
            return self.pkm_ssetdw(pkm, 3, 4, ivs)
        if var == 'specialattackiv':
            ivs = (self.pkm_sgetdw(pkm, 3, 4) & 4294967295L - 32505856) + ((value & 31) << 20)
            return self.pkm_ssetdw(pkm, 3, 4, ivs)
        if var == 'specialdefenseiv':
            ivs = (self.pkm_sgetdw(pkm, 3, 4) & 4294967295L - 1040187392) + ((value & 31) << 25)
            return self.pkm_ssetdw(pkm, 3, 4, ivs)
        if var == 'move1pp':
            return self.pkm_sset(pkm, 1, 8, value)
        if var == 'move1ppup':
            pps = (self.pkm_sget(pkm, 0, 8) & 255 - 3) + ((value & 3) << 0)
            return self.pkm_sset(pkm, 0, 8, pps)
        if var == 'move2pp':
            return self.pkm_sset(pkm, 1, 9, value)
        if var == 'move2ppup':
            pps = (self.pkm_sget(pkm, 0, 8) & 255 - 12) + ((value & 3) << 2)
            return self.pkm_sset(pkm, 0, 8, pps)
        if var == 'move3pp':
            return self.pkm_sset(pkm, 1, 10, value)
        if var == 'move3ppup':
            pps = (self.pkm_sget(pkm, 0, 8) & 255 - 48) + ((value & 3) << 4)
            return self.pkm_sset(pkm, 0, 8, pps)
        if var == 'move4pp':
            return self.pkm_sset(pkm, 1, 11, value)
        if var == 'move4ppup':
            pps = (self.pkm_sget(pkm, 0, 8) & 255 - 192) + ((value & 3) << 6)
            return self.pkm_sset(pkm, 0, 8, pps)
        if var == 'happiness':
            return self.pkm_sset(pkm, 0, 9, value)
        if var == 'pokerus':
            return self.pkm_sset(pkm, 3, 0, value)
        if var == 'caughtlocation':
            return self.pkm_sset(pkm, 3, 1, value)
        if var == 'caughtlevel':
            return self.pkm_sset(pkm, 3, 2, value)
        if var == 'caughtball':
            byte = (self.pkm_sget(pkm, 3, 3) & 135) + ((value & 15) << 3)
            return self.pkm_sset(pkm, 3, 3, byte)
        if var == 'otgender':
            byte = (self.pkm_sget(pkm, 3, 3) & 127) + ((value & 1) << 7)
            return self.pkm_sset(pkm, 3, 3, byte)
        if var == 'maxhp':
            pkm = self.setbyte(88, value & 255, pkm)
            pkm = self.setbyte(89, value >> 8, pkm)
        if var == 'attack':
            pkm = self.setbyte(90, value & 255, pkm)
            pkm = self.setbyte(91, value >> 8, pkm)
        if var == 'defense':
            pkm = self.setbyte(92, value & 255, pkm)
            pkm = self.setbyte(93, value >> 8, pkm)
        if var == 'speed':
            pkm = self.setbyte(94, value & 255, pkm)
            pkm = self.setbyte(95, value >> 8, pkm)
        if var == 'specialattack':
            pkm = self.setbyte(96, value & 255, pkm)
            pkm = self.setbyte(97, value >> 8, pkm)
        if var == 'specialdefense':
            pkm = self.setbyte(98, value & 255, pkm)
            pkm = self.setbyte(99, value >> 8, pkm)
        return pkm

    def setitem(self, x, item, count):
        if x < 163:
            self.gbuffer = self.setbyte(5344 + 4 * x, item & 255, self.gbuffer)
            self.gbuffer = self.setbyte(5345 + 4 * x, item >> 8 & 255, self.gbuffer)
            self.gbuffer = self.setbyte(5346 + 4 * x, count & 255, self.gbuffer)
            self.gbuffer = self.setbyte(5347 + 4 * x, count >> 8 & 255, self.gbuffer)
        if x >= 163:
            x -= 163
            self.gbuffer = self.setbyte(5144 + 4 * x, item & 255, self.gbuffer)
            self.gbuffer = self.setbyte(5145 + 4 * x, item >> 8 & 255, self.gbuffer)
            self.gbuffer = self.setbyte(5146 + 4 * x, count & 255, self.gbuffer)
            self.gbuffer = self.setbyte(5147 + 4 * x, count >> 8 & 255, self.gbuffer)

    def load_money(self):
        money = 0
        money += ord(self.gbuffer[5136])
        money += ord(self.gbuffer[5137]) * 256
        money += ord(self.gbuffer[5138]) * 65536
        chips = 0
        chips += ord(self.gbuffer[5140])
        chips += ord(self.gbuffer[5141]) * 256
        self.money = money
        self.chips = chips

    def load_names(self):
        self.trainerid = ord(self.gbuffer[10]) + ord(self.gbuffer[11]) * 256
        self.name = self.decode(self.gbuffer[0:8])
        self.rivalname = ''

    def decode(self, string):
        decoded = ''
        for c in range(len(string)):
            dec = ord(string[c])
            if self.dtable[dec] != '':
                decoded += self.dtable[dec]
            elif dec == 80:
                return decoded

        return decoded

    def encode(self, string, fill = 0):
        encoded = ''
        for c in range(len(string)):
            dec = ord(string[c])
            if len(self.etable[dec]):
                encoded += self.etable[dec]

        encoded = encoded.ljust(fill, chr(255))
        encoded = encoded[0:fill]
        return encoded
