//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

	PyModule_AddIntConstant (poModule, "CAMERA_TO_POSITIVE",		CPythonApplication::CAMERA_TO_POSITIVE);
	PyModule_AddIntConstant (poModule, "CAMERA_TO_NEGATIVE",		CPythonApplication::CAMERA_TO_NEGITIVE);
	PyModule_AddIntConstant (poModule, "CAMERA_STOP",			CPythonApplication::CAMERA_STOP);

	#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant (poModule, "ENABLE_COSTUME_SYSTEM",	1);
	#else
	PyModule_AddIntConstant (poModule, "ENABLE_COSTUME_SYSTEM",	0);
	#endif

//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_TARGET_INFORMATION_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_TARGET_INFORMATION_SYSTEM", 0);
#endif

//  --------------------------------------------
// |	Son						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------
