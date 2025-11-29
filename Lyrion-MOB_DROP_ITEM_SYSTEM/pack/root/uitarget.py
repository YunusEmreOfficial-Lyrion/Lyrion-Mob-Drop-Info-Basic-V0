##  --------------------------------------------
## |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

import guild
import chr
import nonplayer
import localeInfo
import constInfo

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

if app.ENABLE_TARGET_INFORMATION_SYSTEM:
	import item
	import uiToolTip
	def HAS_FLAG(value, flag):
		return (value & flag) == flag

##  --------------------------------------------
## |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

class TargetBoard(ui.ThinBoard):

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	if app.ENABLE_TARGET_INFORMATION_SYSTEM:
		class InfoBoard(ui.ThinBoard):
			class ItemListBoxItem(ui.ListBoxExNew.Item):
				def __init__(self, width):
					ui.ListBoxExNew.Item.__init__(self)

					image = ui.ExpandedImageBox()
					image.SetParent(self)
					image.Show()
					self.image = image
					self.clickEvent = None 

					nameLine = ui.TextLine()
					nameLine.SetParent(self)
					nameLine.SetPosition(32 + 5, 0)
					nameLine.Show()
					self.nameLine = nameLine

					self.SetSize(width, 32 + 5)

				def LoadImage(self, image, name = None):
					self.image.LoadImage(image)
					self.SetSize(self.GetWidth(), self.image.GetHeight() + 5 * (self.image.GetHeight() / 32))
					if name != None:
						self.SetText(name)

				def SetText(self, text):
					self.nameLine.SetText(text)

				def RefreshHeight(self):
					ui.ListBoxExNew.Item.RefreshHeight(self)
					self.image.SetRenderingRect(0.0, 0.0 - float(self.removeTop) / float(self.GetHeight()), 0.0, 0.0 - float(self.removeBottom) / float(self.GetHeight()))
					self.image.SetPosition(0, - self.removeTop)

			STONE_START_VNUM = 28030
			STONE_LAST_VNUM = 28042

			BOARD_WIDTH = 532

			def __init__(self):
				ui.ThinBoard.__init__(self)

				self.HideCorners(self.LT)
				self.HideCorners(self.RT)
				self.HideLine(self.T)

				self.race = 0
				self.hasItems = False

				self.itemTooltip = uiToolTip.ItemToolTip()
				self.itemTooltip.HideToolTip()

				self.stoneImg = None
				self.stoneVnum = None
				self.lastStoneVnum = 0
				self.nextStoneIconChange = 0

				self.slotSize = 80

				wndItem = ui.GridSlotWindow()
				wndItem.SetParent(self)
				wndItem.ArrangeSlot(0, 16, self.slotSize/16, 32, 32, 0, 0)
				wndItem.RefreshSlot()
				wndItem.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
				wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
				wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
				wndItem.Hide()
				self.wndItem = wndItem
				self.itemArray = [0 for i in xrange(self.slotSize)]
				self.itemVnums = [0 for i in xrange(self.slotSize)]

				self.SetSize(self.BOARD_WIDTH, 0)

			def __del__(self):
				ui.ThinBoard.__del__(self)

			if app.ENABLE_TARGET_INFORMATION_SYSTEM:
				def ShowCorner(self, corner):
					self.Corners[corner].Show()
					self.SetSize(self.GetWidth(), self.GetHeight())

				def HideCorners(self, corner):
					self.Corners[corner].Hide()
					self.SetSize(self.GetWidth(), self.GetHeight())

				def ShowLine(self, line):
					self.Lines[line].Show()
					self.SetSize(self.GetWidth(), self.GetHeight())

				def HideLine(self, line):
					self.Lines[line].Hide()
					self.SetSize(self.GetWidth(), self.GetHeight())

			def __UpdatePosition(self, targetBoard):
				self.SetPosition(targetBoard.GetLeft() + (targetBoard.GetWidth() - self.GetWidth()) / 2, targetBoard.GetBottom() - 16)

			def Open(self, targetBoard, race):
				self.__LoadInformation(race)

				self.SetSize(self.BOARD_WIDTH, self.yPos + 10)
				self.__UpdatePosition(targetBoard)

				self.Show()

			def Refresh(self):
				if self.slotSize > 160:
					self.slotSize = 80
				self.__LoadInformation(self.race)
				tempHeight = ((self.slotSize / 16)-4)*32
				self.SetSize(self.BOARD_WIDTH, self.yPos + 10 + tempHeight)

			def Close(self):
				self.itemTooltip.HideToolTip()
				self.slotSize = 80
				self.Hide()

			def __LoadInformation(self, race):
				self.yPos = 10
				self.children = []
				self.race = race
				self.stoneImg = None
				self.stoneVnum = None
				self.nextStoneIconChange = 0

				for i in xrange(self.slotSize):
					self.wndItem.ClearSlot(i)

				self.wndItem.ArrangeSlot(0, 16, self.slotSize/16, 32, 32, 0, 0)
				self.wndItem.RefreshSlot()
				self.wndItem.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)

				self.itemArray = [0 for i in xrange(self.slotSize)]
				self.itemVnums = [0 for i in xrange(self.slotSize)]

				self.__LoadInformation_Default()
				self.__LoadInformation_Drops(race)

			def __LoadInformation_Default_GetHitRate(self, race):
				attacker_dx = nonplayer.GetMonsterDX(race)
				attacker_level = nonplayer.GetMonsterLevel(race)

				self_dx = player.GetStatus(player.DX)
				self_level = player.GetStatus(player.LEVEL)

				iARSrc = min(90, (attacker_dx * 4 + attacker_level * 2) / 6)
				iERSrc = min(90, (self_dx * 4 + self_level * 2) / 6)

				fAR = (float(iARSrc) + 210.0) / 300.0
				fER = (float(iERSrc) * 2 + 5) / (float(iERSrc) + 95) * 3.0 / 10.0

				return fAR - fER

			def __LoadInformation_Default(self):
				self.AppendSeperator()
				self.AppendTextLine(localeInfo.TARGET_INFO)

			def SerachEmptySlot(self, size):
				
				for value in xrange(self.slotSize):
					
					if 0 == self.itemArray[value]:	# ?????
					
						if 1 == size:
							return value
							
						emptySlotIndex	= value
						searchSucceed	= True
						
						for i in range(size - 1):
							emptySlotIndex = emptySlotIndex + 16
						
							if emptySlotIndex >= self.slotSize:
								searchSucceed = False
								continue
							
							if 1 == self.itemArray[emptySlotIndex]:
								searchSucceed = False
					
						if True == searchSucceed:
							return value
						
				return -1

			def __LoadInformation_Drops(self, race):
				self.AppendSeperator()

				if race in constInfo.MONSTER_INFO_DATA:
					if len(constInfo.MONSTER_INFO_DATA[race]["items"]) == 0:
						self.wndItem.Hide()
						self.AppendTextLine(localeInfo.TARGET_INFO_NO_ITEM_TEXT)

					else:
						self.wndItem.SetPosition(9, self.yPos - 10)
						self.yPos += 32*4-2
						self.SetSize(self.BOARD_WIDTH, self.yPos + 1)
						self.UpdateRect()
						self.wndItem.Show()

						for curItem in constInfo.MONSTER_INFO_DATA[race]["items"]:
							getItemID = 0

							if curItem.has_key("vnum_list"):
								getItemID = curItem["vnum_list"][0]
								vnum = curItem["vnum_list"][0]
							else:
								getItemID = curItem["vnum"]
								vnum=curItem["vnum"]

							getItemCount=curItem["count"]
							item.SelectItem(getItemID)
							itemSize = item.GetItemSize()
							if item.GetItemType() == item.ITEM_TYPE_METIN:
								self.stoneVnum = getItemID
								self.lastStoneVnum = 28430

							emptySlotPos = self.SerachEmptySlot(itemSize[1])

							if -1 != emptySlotPos:
								self.itemArray[emptySlotPos] = 1

								if itemSize[1] == 2:
									self.itemArray[emptySlotPos + 16] = 1
								elif itemSize[1] == 3:
									self.itemArray[emptySlotPos + 16] = 1
									self.itemArray[emptySlotPos + 32] = 1

								if item.GetItemType() == item.ITEM_TYPE_METIN:
									self.stoneImg = emptySlotPos
								self.wndItem.SetItemSlot(emptySlotPos, getItemID, getItemCount)
								self.itemVnums[emptySlotPos] = getItemID
							else:
								if self.slotSize > 160:
									return
								self.slotSize += 16
								self.Refresh()
								return

						self.wndItem.RefreshSlot()
				else:
					self.wndItem.Hide()
					self.AppendTextLine(localeInfo.TARGET_INFO_NO_ITEM_TEXT)

			def OverInItem(self, slotIndex):
				vnum = self.itemVnums[slotIndex]
				if vnum != 0:
					self.OnShowItemTooltip(vnum)

			def OverOutItem(self):
				self.OnHideItemTooltip()

			def AppendTextLine(self, text):
				textLine = ui.TextLine()
				textLine.SetParent(self)
				textLine.SetWindowHorizontalAlignCenter()
				textLine.SetHorizontalAlignCenter()
				textLine.SetText(text)
				textLine.SetPosition(0, self.yPos)
				textLine.Show()

				self.children.append(textLine)
				self.yPos += 17

			def AppendSeperator(self):
				img = ui.ImageBox()
				img.LoadImage("d:/ymir work/ui/seperator.tga")
				self.AppendWindow(img)
				img.SetPosition(img.GetLeft(), img.GetTop() - 16)
				self.yPos -= 11

			def AppendItem(self, listBox, vnums, count):
				if type(vnums) == int:
					vnum = vnums
				else:
					vnum = vnums[0]

				item.SelectItem(vnum)
				itemName = item.GetItemName()
				if type(vnums) != int and len(vnums) > 1:
					vnums = sorted(vnums)
					realName = itemName[:itemName.find("+")]
					if item.GetItemType() == item.ITEM_TYPE_METIN:
						realName = localeInfo.TARGET_INFO_STONE_NAME
						itemName = realName + "+0 - +4"
					else:
						itemName = realName + "+" + str(vnums[0] % 10) + " - +" + str(vnums[len(vnums) - 1] % 10)
					vnum = vnums[len(vnums) - 1]

				myItem = self.ItemListBoxItem(listBox.GetWidth())
				myItem.LoadImage(item.GetIconImageFileName())
				if count <= 1:
					myItem.SetText(itemName)
				else:
					myItem.SetText("%dx %s" % (count, itemName))
				myItem.SAFE_SetOverInEvent(self.OnShowItemTooltip, vnum)
				myItem.SAFE_SetOverOutEvent(self.OnHideItemTooltip)
				listBox.AppendItem(myItem)

				if item.GetItemType() == item.ITEM_TYPE_METIN:
					self.stoneImg = myItem
					self.stoneVnum = vnums
					self.lastStoneVnum = self.STONE_LAST_VNUM + vnums[len(vnums) - 1] % 1000 / 100 * 100

				return myItem.GetHeight()

			def OnShowItemTooltip(self, vnum):
				item.SelectItem(vnum)
				if item.GetItemType() == item.ITEM_TYPE_METIN:
					self.itemTooltip.isStone = True
					self.itemTooltip.isBook = False
					self.itemTooltip.isBook2 = False
					self.itemTooltip.SetItemToolTip(self.lastStoneVnum)
				else:
					self.itemTooltip.isStone = False
					self.itemTooltip.isBook = True
					self.itemTooltip.isBook2 = True
					self.itemTooltip.SetItemToolTip(vnum)

			def OnHideItemTooltip(self):
				self.itemTooltip.HideToolTip()

			def AppendWindow(self, wnd, x = 0, width = 0, height = 0):
				if width == 0:
					width = wnd.GetWidth()
				if height == 0:
					height = wnd.GetHeight()

				wnd.SetParent(self)
				if x == 0:
					wnd.SetPosition((self.GetWidth() - width) / 2, self.yPos)
				else:
					wnd.SetPosition(x, self.yPos)
				wnd.Show()

				self.children.append(wnd)
				self.yPos += height + 5

			def OnUpdate(self):
				if self.stoneImg != None and self.stoneVnum != None and app.GetTime() >= self.nextStoneIconChange:
					nextImg = self.lastStoneVnum + 1
					if nextImg % 100 > self.STONE_LAST_VNUM % 100:
						nextImg -= (self.STONE_LAST_VNUM - self.STONE_START_VNUM) + 1
					self.lastStoneVnum = nextImg
					self.nextStoneIconChange = app.GetTime() + 2.5

					item.SelectItem(nextImg)
					itemName = item.GetItemName()
					realName = itemName[:itemName.find("+")]
					realName = realName + "+0 - +4"
					self.wndItem.SetItemSlot(self.stoneImg, nextImg, 1)

					if self.itemTooltip.IsShow() and self.itemTooltip.isStone:
						self.itemTooltip.SetItemToolTip(nextImg)


##  --------------------------------------------
## |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		closeButton = ui.Button()
		closeButton.SetParent(self)
		closeButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		closeButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		closeButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		closeButton.SetPosition(30, 13)

		if localeInfo.IsARABIC():
			hpGauge.SetPosition(55, 17)
			hpGauge.SetWindowHorizontalAlignLeft()
			closeButton.SetWindowHorizontalAlignLeft()
		else:
			hpGauge.SetPosition(175, 17)
			hpGauge.SetWindowHorizontalAlignRight()
			closeButton.SetWindowHorizontalAlignRight()

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		if app.ENABLE_TARGET_INFORMATION_SYSTEM:
			infoButton = ui.Button()
			infoButton.SetParent(self)
			infoButton.SetUpVisual("d:/ymir work/ui/pattern/q_mark_01.tga")
			infoButton.SetOverVisual("d:/ymir work/ui/pattern/q_mark_02.tga")
			infoButton.SetDownVisual("d:/ymir work/ui/pattern/q_mark_01.tga")
			infoButton.SetEvent(ui.__mem_func__(self.OnPressedInfoButton))
			infoButton.Hide()

			infoBoard = self.InfoBoard()
			infoBoard.Hide()
			infoButton.showWnd = infoBoard

##  --------------------------------------------
## |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		self.buttonDict["VOTE_BLOCK_CHAT"].SetEvent(ui.__mem_func__(self.__OnVoteBlockChat))

		self.name = name
		self.hpGauge = hpGauge

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		if app.ENABLE_TARGET_INFORMATION_SYSTEM:
			self.infoButton = infoButton
			self.vnum = 0

##  --------------------------------------------
## |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		self.__Initialize()
		self.ResetTargetBoard()

	def __del__(self):
		ui.ThinBoard.__del__(self)

		print "===================================================== DESTROYED TARGET BOARD"

	def __Initialize(self):
		self.nameString = ""
		self.nameLength = 0
		self.vid = 0

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		if app.ENABLE_TARGET_INFORMATION_SYSTEM:
			self.vnum = 0

##  --------------------------------------------
## |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		self.isShowButton = False
		self.reload = False

	def Destroy(self):
		self.eventWhisper = None
		self.closeButton = None
		self.showingButtonList = None
		self.buttonDict = None
		self.name = None
		self.hpGauge = None

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		if app.ENABLE_TARGET_INFORMATION_SYSTEM:
			self.infoButton = None

##  --------------------------------------------
## |	Arat hemen altında bro						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		self.__Initialize()

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	if app.ENABLE_TARGET_INFORMATION_SYSTEM:
		def RefreshMonsterInfoBoard(self):
			if not self.infoButton.showWnd.IsShow():
				return

			self.infoButton.showWnd.Refresh()

		def OnPressedInfoButton(self):
			constInfo.MONSTER_INFO_DATA.clear()

			net.SendTargetInfoLoad(player.GetTargetVID())
			if self.infoButton.showWnd.IsShow():
				self.infoButton.showWnd.Close()
			elif self.vnum != 0:
				self.infoButton.showWnd.Open(self, self.vnum)

##  --------------------------------------------
## |	Arat hemen altında bro						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	def OnPressedCloseButton(self):
		player.ClearTarget()
		self.Close()

	def Close(self):
		self.__Initialize()

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		if app.ENABLE_TARGET_INFORMATION_SYSTEM:
			self.infoButton.showWnd.Close()

##  --------------------------------------------
## |	Arat hemen altında bro						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	def ResetTargetBoard(self):

		for btn in self.buttonDict.values():
			btn.Hide()

		self.__Initialize()

		self.name.SetPosition(0, 13)
		self.name.SetHorizontalAlignCenter()
		self.name.SetWindowHorizontalAlignCenter()
		self.hpGauge.Hide()

		self.SetSize(250, 40)

	def SetTargetVID(self, vid):
		self.vid = vid

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		if app.ENABLE_TARGET_INFORMATION_SYSTEM:
			self.vnum = 0

##  --------------------------------------------
## |	Arat hemen altında bro						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	def SetEnemyVID(self, vid):
		self.SetTargetVID(vid)

		name = chr.GetNameByVID(vid)

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		if app.ENABLE_TARGET_INFORMATION_SYSTEM:
			vnum = nonplayer.GetRaceNumByVID(vid)

##  --------------------------------------------
## |	Arat hemen altında bro						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		level = nonplayer.GetLevelByVID(vid)
		grade = nonplayer.GetGradeByVID(vid)

		nameFront = ""
		if -1 != level:
			nameFront += "Lv." + str(level) + " "
		if self.GRADE_NAME.has_key(grade):
			nameFront += "(" + self.GRADE_NAME[grade] + ") "

		self.SetTargetName(nameFront + name)


##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		if app.ENABLE_TARGET_INFORMATION_SYSTEM:
			(textWidth, textHeight) = self.name.GetTextSize()

			self.infoButton.SetPosition(textWidth + 25, 12)
			self.infoButton.SetWindowHorizontalAlignLeft()

			self.vnum = vnum
			self.infoButton.Show()

##  --------------------------------------------
## |	Arat hemen altında bro						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	def SetTargetName(self, name):
		self.nameString = name
		self.nameLength = len(name)
		self.name.SetText(name)

	def SetHP(self, hpPercentage):
		if not self.hpGauge.IsShow():

			self.SetSize(200 + 7*self.nameLength, self.GetHeight())

##  --------------------------------------------
## |	Altına ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

			if app.ENABLE_TARGET_INFORMATION_SYSTEM:
				if chr.GetInstanceType(self.vid) == chr.INSTANCE_TYPE_PLAYER:
					self.infoButton.Hide()
					self.infoButton.showWnd.Close()

##  --------------------------------------------
## |	Son						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------


