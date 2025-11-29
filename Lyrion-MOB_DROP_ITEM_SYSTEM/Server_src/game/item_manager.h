//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

		LPITEM			Find (DWORD id);
		LPITEM                  FindByVID (DWORD vid);
		TItemTable*             GetTable (DWORD vnum);
		bool			GetVnum (const char* c_pszName, DWORD& r_dwVnum);
		bool			GetVnumByOriginalName (const char* c_pszName, DWORD& r_dwVnum);

//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
		bool			CreateDropItemVector(LPCHARACTER pkChr, LPCHARACTER pkKiller, std::vector<LPITEM>& vec_item);
#endif

//  --------------------------------------------
// |	Son							Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------
