##  --------------------------------------------
## |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

		parentWindow = self.GetParentProxy()
		if parentWindow:
			(gx, gy) = parentWindow.GetGlobalPosition()
			x -= gx
			y -= gy

		self.SetPosition(x, y)

class ItemToolTip(ToolTip):

##  --------------------------------------------
## |	Alt©¥na ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	if app.ENABLE_TARGET_INFORMATION_SYSTEM:
		isStone = False
		isBook = False
		isBook2 = False

##  --------------------------------------------
## |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	def AppendTextLine(self, text, color = FONT_COLOR, centerAlign = True):
		if not self.CanEquip() and self.bCannotUseItemForceSetDisableColor:
			color = self.DISABLE_COLOR

		return ToolTip.AppendTextLine(self, text, color, centerAlign)

	def ClearToolTip(self):
		self.isShopItem = False
		self.toolTipWidth = self.TOOL_TIP_WIDTH
		ToolTip.ClearToolTip(self)

##  --------------------------------------------
## |	Alt©¥na Ekle						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	if app.ENABLE_TARGET_INFORMATION_SYSTEM:
		def SetItemToolTipStone(self, itemVnum):
			self.itemVnum = itemVnum
			item.SelectItem(itemVnum)
			itemType = item.GetItemType()

			itemDesc = item.GetItemDescription()
			itemSummary = item.GetItemSummary()
			attrSlot = 0
			self.__AdjustMaxWidth(attrSlot, itemDesc)
			itemName = item.GetItemName()
			realName = itemName[:itemName.find("+")]
			self.SetTitle(realName + " +0 - +4")

			## Description ###
			self.AppendDescription(itemDesc, 26)
			self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)

			if item.ITEM_TYPE_METIN == itemType:
				self.AppendMetinInformation()
				self.AppendMetinWearInformation()

			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)

				if item.LIMIT_REAL_TIME_START_FIRST_USE == limitType:
					self.AppendRealTimeStartFirstUseLastTime(item, metinSlot, i)

				elif item.LIMIT_TIMER_BASED_ON_WEAR == limitType:
					self.AppendTimerBasedOnWearLastTime(metinSlot)

			self.ShowToolTip()

##  --------------------------------------------
## |	Arat						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	def __SetNormalItemTitle(self):
		self.SetTitle(item.GetItemName())

##  --------------------------------------------
## |	De?i?tir						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

	def __SetNormalItemTitle(self):
		if app.ENABLE_TARGET_INFORMATION_SYSTEM:
			if self.isStone:
				itemName = item.GetItemName()
				realName = itemName[:itemName.find("+")]
				self.SetTitle(realName + " +0 - +4")
			else:
				self.SetTitle(item.GetItemName())
		else:
			self.SetTitle(item.GetItemName())

##  --------------------------------------------
## |	Son						Lyrion YunusEmreOfficial v0 Mob drop			|
##  --------------------------------------------

