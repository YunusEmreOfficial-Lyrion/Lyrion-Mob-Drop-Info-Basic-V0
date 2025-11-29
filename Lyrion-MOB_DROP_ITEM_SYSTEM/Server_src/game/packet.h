//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

	HEADER_CG_SAFEBOX_ITEM_MOVE		= 77,
	HEADER_CG_PARTY_PARAMETER		= 78,
	//HEADER_BLANK68					= 79,
	HEADER_CG_GUILD					= 80,
	HEADER_CG_ANSWER_MAKE_GUILD		= 81,
	HEADER_CG_FISHING				= 82,
	HEADER_CG_GIVE_ITEM				= 83,
	//HEADER_BLANK84					= 84,
	//HEADER_BLANK85					= 85,
	//HEADER_BLANK86					= 86,
	//HEADER_BLANK87					= 87,
	//HEADER_BLANK88					= 88,
	//HEADER_BLANK89					= 89,

//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
	HEADER_CG_TARGET_INFO_LOAD = 89, // Paket nuamars©¥ varsa de?i?tir knks
#endif

//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

	// MINING
	HEADER_GC_DIG_MOTION				= 134,
	// END_OF_MINING
	HEADER_GC_DAMAGE_INFO				= 135,
	HEADER_GC_CHAR_ADDITIONAL_INFO		= 136,
	// SUPPORT_BGM
	HEADER_GC_MAIN_CHARACTER3_BGM		= 137,
	HEADER_GC_MAIN_CHARACTER4_BGM_VOL	= 138,
	// END_OF_SUPPORT_BGM

//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
	HEADER_GC_TARGET_INFO = 140, // Bu paket numaras©¥ varsa de?i?tir.
#endif

//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

typedef struct SPacketCGStateCheck
{
	BYTE header;
	unsigned long key;
	unsigned long index;
} TPacketCGStateCheck;

typedef struct SPacketGCStateCheck
{
	BYTE header;
	unsigned long key;
	unsigned long index;
	unsigned char state;
} TPacketGCStateCheck;

//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
typedef struct packet_target_info
{
	BYTE	header;
	DWORD	dwVID;
	DWORD	race;
	DWORD	dwVnum;
	BYTE	count;
} TPacketGCTargetInfo;

typedef struct packet_target_info_load
{
	BYTE header;
	DWORD dwVID;
} TPacketCGTargetInfoLoad;
#endif

//  --------------------------------------------
// |	Son						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------
