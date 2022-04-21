package UtilMethods;

import java.lang.reflect.Array;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Util methods for cleaning up the main class rather than nesting 198237 conditionals
 */
public class MainUtilMethods {

    /**
     * Iterate through the file
     */
    public static boolean validArgumentNames(String fieldName){
        ArrayList<String> argNames = new ArrayList<>(Arrays.asList("covid", "properties", "population", "log"));
        return argNames.contains(fieldName);
    }

    /**
     * Iterate through the runTimeFiles and see if the same name field gets uses more than once
     * @param runtimeFiles: Array List of file types and names
     * @return boolean for if there's a duplicate or there's an invalid name in there
     */
    public static boolean checkArgumentNames(ArrayList<String> runtimeFiles){
        ArrayList<String> other = new ArrayList<>();
        for (int i = 0; i < runtimeFiles.size(); i++){
            if (i % 2 == 0){
                // Check if it's a valid name for a field, ex: covid
                if (!validArgumentNames(runtimeFiles.get(i))){
                    return false;
                }
                other.add(runtimeFiles.get(i));
            }
        }

        Set<String> nameFields = new HashSet<>(other);
        // Compare the size of the set to the size of the ArrayList
        return nameFields.size() == other.size();
    }

    /**
     * Match each arg on the regex pattern
     * @param args: The runtime args for the program
     */
    public static ArrayList<String> getRuntimeFiles(String[] args){
        ArrayList<String> runtimeFiles = new ArrayList<>();

        for (String files : args){
            // Match on the regex pattern
            Pattern fileRegex = Pattern.compile("^--(?<name>.+?)=(?<value>.+)$");
            Matcher match = fileRegex.matcher(files);
            while (match.find()){
                // Add the name of the argument and the argument to a Map
                runtimeFiles.add(match.group(1).toLowerCase().trim());
                runtimeFiles.add(match.group(2));
            }
        }

        return runtimeFiles;
    }

    public static String getFileType(String filename){
        return filename.substring(filename.length() - 4);
    }

    public static boolean isJsonFileType(String filename){
        var fileEnding = getFileType(filename);
        return fileEnding.equals("json");
    }


    public static boolean isCsvFileType(String filename){
        var fileEnding = getFileType(filename);
        return fileEnding.equals(".csv");
    }


    public static void printOptions(){
        String options = """
        1. Exit the program
        2. Show the available data sets
        3. Show the population for all Zip code
        4. Show the total vaccinations per capita for each Zip code on the specified date
        5. Show the total average livable area for properties in a specified Zip Code
        6. Show the total market value of properties, per capita, for a specified ZIP Code
        7. Show the results of <insert custom feature>""";
        System.out.println(options);
    }

    /**
     * Notes:
     * 1. Show avail data sets = return all the parsed file names or the key map pairing
     * 2. Show to population
     */


    /**
     * Things that I still need to do
     * - Any arg that doesn't match the form --name=value
     * - Name of the argument does not match the names (validArg) [DONE]
     * - Name of the arg is used more than once [DONE]
     * - Logger can't be init (invalid string given as log file name)?
     * - file format isn't valid ".csv" or "json"
     * - Can't be opened because of file permissions
     */


    public static void parseArguments(){}

    public static void validArguments(){}

}
