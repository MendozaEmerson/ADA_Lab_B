
# Emerson Danny Mendoza Hilasaca
# 5. What is the time complexity in terms of O()?
# O(log_2(n))
# resumes is an array
def pick_resume(resumes):
    eliminate = "top"
    
    while resumes.length > 1:
        if eliminate == "top":
            resumes = resumes[resumes.length / 2, resumes.length - 1]
            eliminate = "bottom"
        elif eliminate == "bottom":
            resumes = resumes[0, resumes.length / 2]
            eliminate = "top"
        end
    end
    return resumes[0]
end

# La conplejidad se debe a la llamada recursiva que se hace del valor reducido en los dos posibles casos.