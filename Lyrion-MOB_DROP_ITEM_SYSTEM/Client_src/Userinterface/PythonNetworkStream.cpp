//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

			Set (HEADER_GC_SAFEBOX_SET,	CNetworkPacketHeaderMap::TPacketType (sizeof (TPacketGCItemSet), STATIC_SIZE_PACKET));
			Set (HEADER_GC_SAFEBOX_DEL,	CNetworkPacketHeaderMap::TPacketType (sizeof (TPacketGCItemDel), STATIC_SIZE_PACKET));
			Set (HEADER_GC_SAFEBOX_WRONG_PASSWORD,	CNetworkPacketHeaderMap::TPacketType (sizeof (TPacketGCSafeboxWrongPassword), STATIC_SIZE_PACKET));
			Set (HEADER_GC_SAFEBOX_SIZE,	CNetworkPacketHeaderMap::TPacketType (sizeof (TPacketGCSafeboxSize), STATIC_SIZE_PACKET));
			Set (HEADER_GC_SAFEBOX_MONEY_CHANGE,	CNetworkPacketHeaderMap::TPacketType (sizeof (TPacketGCSafeboxMoneyChange), STATIC_SIZE_PACKET));

			Set (HEADER_GC_FISHING,	CNetworkPacketHeaderMap::TPacketType (sizeof (TPacketGCFishing), STATIC_SIZE_PACKET));
			Set (HEADER_GC_DUNGEON, CNetworkPacketHeaderMap::TPacketType (sizeof (TPacketGCDungeon), DYNAMIC_SIZE_PACKET));
			//Set(HEADER_GC_SLOW_TIMER, CNetworkPacketHeaderMap::TPacketType(sizeof(BYTE), STATIC_SIZE_PACKET));


//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
			Set(HEADER_GC_TARGET_INFO, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCTargetInfo), false));
#endif

//  --------------------------------------------
// |	Son						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------
