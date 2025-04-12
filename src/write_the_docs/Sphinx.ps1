param([string]$Path, [string]$Project, [string]$Author, [string]$Version, [string]$Release, [string]$OutputDir)

Set-Location $Path
sphinx-apidoc . -o $OutputDir -f -l -F -H $Project -A $Author -V $Version -R $Release 
Set-Location $OutputDir 
sphinx-build . _build


