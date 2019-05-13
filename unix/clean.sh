# ------------------------------------------------------------
# Housekeeping
# recursively rename all files to lowercase
find . -depth -print -execdir rename -f 'y/A-Z/a-z/' '{}' \;

# replace all substr in file name recursively
# update -name "*-*" and "${base//-/_}" to replace
# This example replace - with _
find . -name "*-*" \
| awk '{ print length, $0 }' \
| sort -nr -s \
| cut -d" " -f2- \
| while read f; \
do base=$(basename "$f"); \
newbase="${base//-/_}"; \
mv "$(dirname "$f")/$(basename "$f")" "$(dirname "$f")/$newbase"; \
done

find . -name "* *" \
| awk '{ print length, $0 }' \
| sort -nr -s \
| cut -d" " -f2- \
| while read f; \
do base=$(basename "$f"); \
newbase="${base// /_}"; \
mv "$(dirname "$f")/$(basename "$f")" "$(dirname "$f")/$newbase"; \
done

find . -name "*__*" \
| awk '{ print length, $0 }' \
| sort -nr -s \
| cut -d" " -f2- \
| while read f; \
do base=$(basename "$f"); \
newbase="${base/__/_}"; \
mv "$(dirname "$f")/$(basename "$f")" "$(dirname "$f")/$newbase"; \
done

find . -name "*__*" \
| awk '{ print length, $0 }' \
| sort -nr -s \
| cut -d" " -f2- \
| while read f; \
do base=$(basename "$f"); \
newbase="${base/__/_}"; \
mv "$(dirname "$f")/$(basename "$f")" "$(dirname "$f")/$newbase"; \
done

find . -name "*__*" \
| awk '{ print length, $0 }' \
| sort -nr -s \
| cut -d" " -f2- \
| while read f; \
do base=$(basename "$f"); \
newbase="${base/__/_}"; \
mv "$(dirname "$f")/$(basename "$f")" "$(dirname "$f")/$newbase"; \
done
