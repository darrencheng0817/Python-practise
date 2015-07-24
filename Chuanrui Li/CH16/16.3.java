
//locker problems
void eat(){
    if(pickup()){
        chew();
        putDown();
    }
}

//pick up function
void boolean pickup(){
    if(!left.pickup()){
        return false;
    }
    if(!right.pickup()){
        left.putDown();
        return false;
    }
    return true;
}