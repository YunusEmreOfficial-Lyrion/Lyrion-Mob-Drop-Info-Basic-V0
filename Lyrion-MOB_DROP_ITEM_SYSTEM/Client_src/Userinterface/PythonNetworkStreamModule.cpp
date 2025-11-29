//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

PyObject* netConnectToAccountServer (PyObject* poSelf, PyObject* poArgs)
{
	char* addr;
	if (!PyTuple_GetString (poArgs, 0, &addr))
	{
		return Py_BuildException();
	}

	int port;
	if (!PyTuple_GetInteger (poArgs, 1, &port))
	{
		return Py_BuildException();
	}

	char* account_addr;
	if (!PyTuple_GetString (poArgs, 2, &account_addr))
	{
		return Py_BuildException();
	}

	int account_port;
	if (!PyTuple_GetInteger (poArgs, 3, &account_port))
	{
		return Py_BuildException();
	}

	CAccountConnector& rkAccountConnector = CAccountConnector::Instance();
	rkAccountConnector.Connect (addr, port, account_addr, account_port);
	return Py_BuildNone();
}

//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
PyObject* netTargetInfoLoad(PyObject* poSelf, PyObject* poArgs)
{
	DWORD dwVID;
	if (!PyArg_ParseTuple(poArgs, "i", &dwVID))
	{
		return Py_BuildException();
	}
	if (dwVID < 0)
	{
		return Py_BuildNone();
	}
	CPythonNetworkStream& rns = CPythonNetworkStream::Instance();
	rns.SendTargetInfoLoadPacket(dwVID);
	return Py_BuildNone();
}
#endif

//  --------------------------------------------
// |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

		// FIELD_MUSIC
		{ "GetFieldMusicFileName",				netGetFieldMusicFileName,				METH_VARARGS },
		{ "GetFieldMusicVolume",				netGetFieldMusicVolume,					METH_VARARGS },
		// END_OF_FIELD_MUSIC

		{ "ToggleGameDebugInfo",				netToggleGameDebugInfo,					METH_VARARGS },


//  --------------------------------------------
// |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------

#ifdef ENABLE_TARGET_INFORMATION_SYSTEM
		{ "SendTargetInfoLoad", 				netTargetInfoLoad, 						METH_VARARGS },
#endif

//  --------------------------------------------
// |	Son						Lyrion YunusEmreOfficial v0 Mob drop			|
//  --------------------------------------------
