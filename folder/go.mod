module folder

require (
	folder/a v0.0.0
)

go 1.22

replace (
	folder/a v0.0.0 => ./a
)