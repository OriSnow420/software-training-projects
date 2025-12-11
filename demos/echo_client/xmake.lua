add_rules("mode.debug", "mode.release")

add_requires("libhv >=1.3.3", {configs = {http_server = false}})

target("main")
    set_kind("binary")
    add_packages("libhv")
    add_files("main.cpp")
    set_languages("cxx20")
    set_exceptions("cxx")

    if is_plat("windows") then
        add_defines("NOMINMAX")
    end

    after_build(function (target)
        os.cp(
            target:targetfile(), 
            path.join(os.projectdir(), "bin", path.filename(target:targetfile()))
        )
    end)
