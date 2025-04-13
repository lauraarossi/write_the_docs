param(
    [Parameter(Mandatory=$True, Position = 0)][string]$Path, 
    [Parameter(Mandatory=$True, Position = 1)][string]$Project, 
    [Parameter(Mandatory=$True, Position = 2)][string]$Author, 
    [Parameter(Mandatory=$True, Position = 3)][string]$Version, [string]$Release, 
    [Parameter(Mandatory=$True, Position = 4)][string]$OutputDir, 
    [Parameter(ValueFromRemainingArguments = $true)]$OtherValues
    )

Set-Location $Path
sphinx-apidoc . -o $OutputDir -f -l -F -H $Project -A $Author -V $Version -R $Release $OtherValues
Set-Location $OutputDir 
sphinx-build . _build


