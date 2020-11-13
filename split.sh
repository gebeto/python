DEPLOY_FOLDER_PATH="$1"
DEPLOY_BRANCH="$DEPLOY_FOLDER_PATH"
DEPLOY_GIT_URL="https://github.com/$2"

echo "Split folder '$DEPLOY_FOLDER_PATH' to '$DEPLOY_GIT_URL'."

git subtree split --prefix $DEPLOY_FOLDER_PATH -b $DEPLOY_FOLDER_PATH
git remote add $DEPLOY_FOLDER_PATH $DEPLOY_GIT_URL
git push --force $DEPLOY_FOLDER_PATH $DEPLOY_BRANCH:main
git branch -D $DEPLOY_BRANCH
git remote remove $DEPLOY_FOLDER_PATH