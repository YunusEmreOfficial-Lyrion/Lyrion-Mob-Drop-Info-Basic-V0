//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

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
	HEADER_CG_TARGET_INFO_LOAD = 89, // Bu numara ba?ka pakete tan©¥mlysa de?i?tir.
#endif

//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

	HEADER_GC_TIME						= 106,
	HEADER_GC_CHANGE_NAME				= 107,
	HEADER_GC_DUNGEON					= 110,
	HEADER_GC_WALK_MODE					= 111,
	HEADER_GC_CHANGE_SKILL_GROUP		= 112,
	#if defined(GAIDEN)
	HEADER_GC_MAIN_CHARACTER			= 113,
	HEADER_GC_MAIN_CHARACTER3_BGM		= 137,
	HEADER_GC_MAIN_CHARACTER4_BGM_VOL	= 138,
	#else

//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
	HEADER_GC_TARGET_INFO = 140, // Varsa de?i?tir.
#endif

//  --------------------------------------------
// |	Ara						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

typedef struct SPacketCGDragonSoulRefine
{
	SPacketCGDragonSoulRefine() : header (HEADER_CG_DRAGON_SOUL_REFINE)
	{}
	BYTE header;
	BYTE bSubType;
	TItemPos ItemGrid[DS_REFINE_WINDOW_MAX_NUM];
} TPacketCGDragonSoulRefine;

typedef struct SPacketGCDragonSoulRefine
{
	SPacketGCDragonSoulRefine() : header (HEADER_GC_DRAGON_SOUL_REFINE)
	{}
	BYTE header;
	BYTE bSubType;
	TItemPos Pos;
} TPacketGCDragonSoulRefine;

typedef struct SChannelStatus
{
	short nPort;
	BYTE bStatus;
} TChannelStatus;

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
