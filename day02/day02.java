import java.io.*;
import java.util.*;

class Day02 {
    static class Password {
        int min;
        int max;
        String passwd_char;

        String passwd;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Vector<Password> pwd_vec = new Vector<Password>();

        while (scanner.hasNext()) {
            String in = scanner.nextLine();
            Password curr_pwd = new Password();

            //System.out.println(in);

            curr_pwd.min         = Integer.parseInt(in.substring(                  0, in.indexOf('-')));
            curr_pwd.max         = Integer.parseInt(in.substring(in.indexOf('-') + 1, in.indexOf(' ')));
            curr_pwd.passwd_char = in.substring(in.indexOf(' ') + 1, in.indexOf(':'));
            curr_pwd.passwd      = in.substring(in.indexOf(':') + 2);

            pwd_vec.add(curr_pwd);
        }


        int correct_pwd_count = 0;
        int other_correct_pwd_count = 0;

        for (Password pwd : pwd_vec) {
            int match_count = pwd.passwd.length() - pwd.passwd.replace(new String(pwd.passwd_char), "").length();

            int min = Math.min(pwd.min-1, pwd.passwd.length());
            int max = Math.min(pwd.max-1, pwd.passwd.length());

            if (pwd.min <= match_count && match_count <= pwd.max)
                ++correct_pwd_count;

            //System.out.println(pwd.passwd + " " + min + "-" + max);

            if (  pwd.passwd.startsWith(pwd.passwd_char, min)
                ^ pwd.passwd.startsWith(pwd.passwd_char, max))
                ++other_correct_pwd_count;
        }
        System.out.println("Part 1: " + correct_pwd_count);
        System.out.println("Part 2: " + other_correct_pwd_count);


    }
}


