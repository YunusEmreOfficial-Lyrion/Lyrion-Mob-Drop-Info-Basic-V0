//  --------------------------------------------
// |	Uste ekle #includelerin aras©¥na						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
#include <algorithm>
#include <iterator>
using namespace std;
#endif

//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

	m_fAttMul = 1.0f;
	m_fDamMul = 1.0f;
	m_pointsInstant.iDragonSoulActiveDeck = -1;

	memset (&m_tvLastSyncTime, 0, sizeof (m_tvLastSyncTime));
	m_iSyncHackCount = 0;


//  --------------------------------------------
// |	Alt©¥na ekle }'den oncesine						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
	dwLastTargetInfoPulse = 0;
#endif

//  --------------------------------------------
// |	Son						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------
