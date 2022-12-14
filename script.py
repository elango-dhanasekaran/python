import os
import xml.etree.ElementTree as ET
import json

parent_dir = [
    name
    for name in os.listdir("./")
    if os.path.isdir(name) and not name.startswith(".")
][0]
# print(parent_dir)
outdict = {
    "proxy-copy": {"ProxiesPreflowPolicies": [], "ProxiesPostflowPolicies": []},
    "proxy": {"ProxiesPreflowPolicies": [], "ProxiesPostflowPolicies": []},
}
sub_dirs = os.listdir("./" + parent_dir + "/")
print("sub_dirs", sub_dirs)
for dir in sub_dirs:
    path = f"./{parent_dir}/{dir}/proxies/"
    print("path", path)
    file_required = [f for f in os.listdir(path) if os.path.isfile(path + f)][0]
    tree = ET.parse(path + file_required)
    root = tree.getroot()
    for item in root:
        if item.attrib.get("name") == "PostFlow":
            for sub_item in item:
                for step in sub_item:
                    if "proxyName - Copy" in path:
                        outdict["proxy-copy"]["ProxiesPostflowPolicies"].append(
                            step[0].text.strip()
                        )
                    else:
                        outdict["proxy"]["ProxiesPostflowPolicies"].append(
                            step[0].text.strip()
                        )
        elif item.attrib.get("name") == "PreFlow":
            for sub_item in item:
                for step in sub_item:
                    if "proxyName - Copy" in path:
                        outdict["proxy-copy"]["ProxiesPreflowPolicies"].append(
                            step[0].text.strip()
                        )
                    else:
                        outdict["proxy"]["ProxiesPreflowPolicies"].append(
                            step[0].text.strip()
                        )


# print(outdict)

with open("proxy_defs.json", "r") as fi:
    data_dict = json.load(fi)
    data_dict["sada-chouse-test"]["Policies"] = outdict["proxy"]
    data_dict["test2"]["Policies"] = outdict["proxy-copy"]

with open("output.json", "w") as fi:
    json.dump(data_dict, fi, indent=4)
# print(json.dumps(data_dict, indent=4))
