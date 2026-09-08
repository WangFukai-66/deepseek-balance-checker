on run {input, parameters}
	tell application "Microsoft Edge"
		open POSIX file "（你的autocue.html的路径）"
		activate
	end tell
	return input
end run
