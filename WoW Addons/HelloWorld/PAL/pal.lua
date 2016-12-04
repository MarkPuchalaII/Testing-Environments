PAL_Text = {}
local channel = "SAY"

SLASH_PAL_ADD1 = "/padd"
SLASH_PAL_ADD2 = "/paladd" -- an alias for /hwadd
SlashCmdList["PAL_ADD"] = function(msg)
  local id, text = msg:match("(%S+)%s+(.+)")
  if id and text then
    PAL_Text[id:lower()] = text
  else
    print("Usage: /hwadd <id> <text>")
  end
end

SLASH_PAL_SHOW1 = "/pshow"
SLASH_PAL_SHOW2 = "/palshow" -- an alias for /hwshow
SlashCmdList["PAL_SHOW"] = function(msg)
  local text = PAL_Text[msg:lower()]
  if text then
    SendChatMessage(text, channel) -- function SeNdChatMessage(msg, channel, language, target)
  end -- msg      = "Your message"
end   -- channel  = SAY(default), YELL, EMOTE, WHISPER, PARTY, RAID, BATTLEGROUND, RAID WARNING, GUILD, OFFICER
      -- language = Language to use (nil uses character's default language)
      -- target   = only needed for channel = WHISPER
