import subprocess

try:
    from packaging.requirements import Requirement
    from packaging.version import Version
except ModuleNotFoundError:
    print("Installing required library: packaging")
    subprocess.check_call(["uv", "pip", "install", "packaging"])
    from packaging.requirements import Requirement
    from packaging.version import Version

from importlib.metadata import distributions

def check_dependencies():
    print("Checking packages...")

    with open("requirements.txt") as f:
        required = [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

    installed = {
        dist.metadata["Name"].lower(): dist.version
        for dist in distributions()
        if dist.metadata.get("Name")
    }

    missing_or_outdated = []

    for req in required:
        try:
            requirement = Requirement(req)
        except Exception as e:
            print(f"⚠️ Error parsing requirement: {req}")
            continue

        name = requirement.name.lower()
        installed_version = installed.get(name)

        if installed_version is None:
            missing_or_outdated.append(req)
            continue

        if requirement.specifier:
            if Version(installed_version) not in requirement.specifier:
                missing_or_outdated.append(req)

    if missing_or_outdated:
        print("Installing missing or outdated packages:")
        print(", ".join(missing_or_outdated))

        subprocess.check_call(
            ["uv", "pip", "install", *missing_or_outdated]
        )
    else:
        print("All dependencies satisfied.")

check_dependencies()