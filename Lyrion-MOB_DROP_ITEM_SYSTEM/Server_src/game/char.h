//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

	public:
		CHARACTER();
		virtual ~CHARACTER();

		void			Create (const char* c_pszName, DWORD vid, bool isPC);
		void			Destroy();

		void			Disconnect (const char* c_pszReason);

	protected:
		void			Initialize();

//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
	private:
			DWORD			dwLastTargetInfoPulse;

	public:
			DWORD			GetLastTargetInfoPulse() const { return dwLastTargetInfoPulse; }
			void			SetLastTargetInfoPulse(DWORD pulse) { dwLastTargetInfoPulse = pulse; }
#endif

//  --------------------------------------------
// |	Son						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------
