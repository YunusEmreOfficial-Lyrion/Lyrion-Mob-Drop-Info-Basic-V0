//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

	Set (HEADER_CG_SCRIPT_SELECT_ITEM,	sizeof (TPacketCGScriptSelectItem),	"ScriptSelectItem",		true);
	Set (HEADER_CG_DRAGON_SOUL_REFINE,	sizeof (TPacketCGDragonSoulRefine),	"DragonSoulRefine",		false);
	Set (HEADER_CG_STATE_CHECKER,		sizeof (BYTE),						"ServerStateCheck",		false);

//  --------------------------------------------
// |	Altına ekle }'den öncesine						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
	Set(HEADER_CG_TARGET_INFO_LOAD, sizeof(TPacketCGTargetInfoLoad), "TargetInfoLoad");
#endif

//  --------------------------------------------
// |	Son						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------
