# Настройка PyCharm для совместной работы с GitHub

Делается один раз в начале работы.

## Зарегистрируйте новый аккаунт на github.com

Это можно сделать, используя ваш google account.

## Создайте новый репозиторий на github.com

Делайте с файлами `README.md` и `.gitignore` (надо будет поставить галочки, в инструкции написано).

[Инструкция по созданию нового репозитория](https://vertex-academy.com/tutorials/ru/kak-sozdat-repozitorij-na-github/)

## Создайте новый проект в PyCharm

[Инструкция по созданию нового проекта](https://metanit.com/python/tutorial/1.3.php)

## Настройте связь проекта и github.com

1. Выберите в проекте систему контроля версий. Откройте в PyCharm меню `VSC / Enable Version Control Integration`. 

![pycharm_vsc_1.png](https://github.com/tatyderb/python_myanmar/blob/master/lectures/img/pycharm_vsc_1.png?raw=true)

В диалоговом окне выберите `Git` и нажмите `Ok`. 

![pycharm_vsc_2.png](https://github.com/tatyderb/python_myanmar/blob/master/lectures/img/pycharm_vsc_2.png?raw=true)

Меню должно измениться на `Git`

![pycharm_vsc_3.png](https://github.com/tatyderb/python_myanmar/blob/master/lectures/img/pycharm_vsc_3.png?raw=true)

2. Откройте в PyCharm меню `File / Settings / Version Control / Git`. 

3. Добавьте свой аккаунт. Нажмите `Add account` и выберите `Log in with Token` 

![pycharm_git_1.png](https://raw.githubusercontent.com/tatyderb/python_myanmar/master/lectures/img/pycharm_git_1.png)

4. Нажмите кнопку `Generate`

![pycharm_git_2.png](https://raw.githubusercontent.com/tatyderb/python_myanmar/master/lectures/img/pycharm_git_2.png)

5. Генерация токена в github.com

В браузере откроется страница генерации токена. Настройте время его действия. В учебном классе на летней практике не более 30 дней. На личном компьютере можно установить `No expiration` (бессрочный).

Другие настройки оставьте по умолчанию.

Отмотайте страницу вниз и нажмите кнопку `Generate token`.

![pycharm_git_3.png](https://raw.githubusercontent.com/tatyderb/python_myanmar/master/lectures/img/pycharm_git_3.png)

![pycharm_git_4.png](https://raw.githubusercontent.com/tatyderb/python_myanmar/master/lectures/img/pycharm_git_4.png)

6. Скопируйте полученный токен.

![pycharm_git_5.png](https://raw.githubusercontent.com/tatyderb/python_myanmar/master/lectures/img/pycharm_git_5.png)

7. Вставьте скопированный токен в окне PyCharm и нажмите кнопку `Add Account`. 

![pycharm_git_6.png](https://raw.githubusercontent.com/tatyderb/python_myanmar/master/lectures/img/pycharm_git_6.png)

Ваш логин добавится в список. Не забудьте нажать `Ок`.

![pycharm_git_7.png](https://raw.githubusercontent.com/tatyderb/python_myanmar/master/lectures/img/pycharm_git_7.png)

8. Перейдите в браузере на страницу вашего проекта на github. Скопируйте URL вашего репозитория. Выбрать `SSH`!

![git_url.png](https://raw.githubusercontent.com/tatyderb/python_myanmar/master/lectures/img/git_url.png)

9. В PyCharm выберите меню `Git / Clone...`

Вставьте скопированный URL репозитория в поле `URL`. Проверьте, что директория выбрана правильная и нажмите `Ok`.

![git_url_pycharm.png](https://raw.githubusercontent.com/tatyderb/python_myanmar/master/lectures/img/git_url_pycharm.png)

10. Убедитесь, что в списке файлов проекта появился файл `README.md`, если вы его сделали на этапе создания репозитория.

11. Добавьте в файл `.gitignore` правило, что не нужно хранить служебную информацию PyCharm в репозитории.

```python
.idea/
```

# Регулярная работа с git

* workspace - ваше рабочее пространство (файлы и директории)
* repository (репозиторий) - в нем хранятся **изменения** файлов
* stash (сундучок) - туда можно отложить некоторые изменения

![локальный и удаленный репозитории](https://static.javatpoint.com/tutorial/git/images/git-pull2.png)

* `add` - добавить файл в репозиторий или *пометить файл, что он будет включен в коммит*
* `commit` - зафиксировать изменения в локальном репозитории
* `push` - донести уже зафиксированные изменения до удаленного репозитория
* `pull` - взять изменения с удаленного репозитория

Предполагаем, что вы работаете на разных компьютерах - один в учебном классе, другой дома.

1. В начале работы сделайте **pull**, выбрав в меню `GIT / Pull`.
2. Изменяйте файлы.
3. Перейдите на панель `Commit`. Отметьте нужные файлы, впишите название коммита (о чем он) и нажмите кнопку `Commit` (зафиксировать изменения локально) или `Commit and Push...` (и локально, и послать на github).
4. повторяем пункты 2 и 3, не забываем коммититься после каждого существенного изменения, а не "раз в три дня".
5. **В конце работы обязательно сделайте `push`**






